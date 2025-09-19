#!/usr/bin/env python3
"""
Script to extract Waze links from HTML anchor tags in CSV file.
Processes the Jerusalem Shelters CSV file and extracts clean Waze URLs.
"""

import csv
import re
from urllib.parse import unquote
import argparse
import os


def extract_waze_url(html_content):
    """
    Extract the Waze URL from HTML anchor tag content.
    
    Args:
        html_content (str): HTML content containing anchor tag with Waze link
        
    Returns:
        str: Clean Waze URL or original content if no URL found
    """
    if not html_content or not isinstance(html_content, str):
        return html_content
    
    # Pattern to match href attribute in anchor tags
    href_pattern = r'href=["\']([^"\']*)["\']'
    
    matches = re.findall(href_pattern, html_content)
    
    for match in matches:
        # Decode HTML entities and URL encoding
        decoded_url = unquote(match)
        
        # Check if it's a Waze URL
        if 'waze.com' in decoded_url or 'ul.waze.com' in decoded_url:
            return decoded_url
        elif 'goo.gl/maps' in decoded_url:
            # Handle Google Maps redirects that might be Waze links
            return decoded_url
    
    # If no Waze URL found, return original content
    return html_content


def process_csv_file(input_file, output_file=None):
    """
    Process the CSV file to extract Waze links from the waze_link column.
    
    Args:
        input_file (str): Path to input CSV file
        output_file (str): Path to output CSV file (optional)
    """
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        return
    
    # Generate output filename if not provided
    if output_file is None:
        base_name = os.path.splitext(input_file)[0]
        output_file = f"{base_name}_extracted_waze_links.csv"
    
    processed_rows = []
    waze_links_extracted = 0
    
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            # Use csv.Sniffer to detect delimiter
            sample = infile.read(1024)
            infile.seek(0)
            sniffer = csv.Sniffer()
            delimiter = sniffer.sniff(sample).delimiter
            
            reader = csv.DictReader(infile, delimiter=delimiter)
            
            # Get the fieldnames
            fieldnames = reader.fieldnames
            
            if 'waze_link' not in fieldnames:
                print("Error: 'waze_link' column not found in CSV file.")
                print(f"Available columns: {', '.join(fieldnames)}")
                return
            
            print(f"Processing {input_file}...")
            print(f"Found columns: {', '.join(fieldnames)}")
            
            for row_num, row in enumerate(reader, start=2):  # Start at 2 since header is row 1
                original_waze_link = row['waze_link']
                extracted_url = extract_waze_url(original_waze_link)
                
                # Update the row with extracted URL
                row['waze_link'] = extracted_url
                
                # Track if we extracted a URL (i.e., it changed from HTML to URL)
                if extracted_url != original_waze_link and 'waze.com' in extracted_url:
                    waze_links_extracted += 1
                
                processed_rows.append(row)
                
                # Progress indicator
                if row_num % 50 == 0:
                    print(f"Processed {row_num - 1} rows...")
        
        # Write the processed data to output file
        with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(processed_rows)
        
        print(f"\nProcessing complete!")
        print(f"Total rows processed: {len(processed_rows)}")
        print(f"Waze links extracted: {waze_links_extracted}")
        print(f"Output saved to: {output_file}")
        
        # Show some examples of extracted URLs
        print("\nSample extracted URLs:")
        count = 0
        for row in processed_rows[:5]:
            if 'waze.com' in row['waze_link'] and not row['waze_link'].startswith('<a'):
                print(f"  - {row['waze_link']}")
                count += 1
                if count >= 3:
                    break
    
    except Exception as e:
        print(f"Error processing file: {e}")


def main():
    """Main function to handle command line arguments and execute the script."""
    parser = argparse.ArgumentParser(
        description="Extract Waze links from HTML anchor tags in CSV file"
    )
    parser.add_argument(
        "input_file",
        nargs="?",
        help="Path to the input CSV file containing HTML anchor tags with Waze links"
    )
    parser.add_argument(
        "-o", "--output",
        help="Path to the output CSV file (default: input_file_extracted_waze_links.csv)"
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="Run a test on a few sample entries to verify extraction"
    )
    
    args = parser.parse_args()
    
    if args.test:
        # Test the extraction function with sample data
        test_samples = [
            '<a rel="noopener" href="https://www.waze.com/ul?ll=31.79069840%2C35.22133660&amp;navigate=yes&amp;zoom=16" target="_blank">25 Yoel St.</a>',
            '<a rel="noopener" href="https://ul.waze.com/ul?place=ChIJu7pxf90pAxURLAhuO0f2chM&amp;ll=31.79247020%2C35.22314580&amp;navigate=yes" target="_blank">61 Shmuel Hanavi St.</a>',
            '<a rel="noopener" href="https://goo.gl/maps/DBvHPN7VXXp?ll=31.75982140%2C35.22352620&amp;navigate=yes&amp;zoom=16" target="_blank">6 Esther HaMalka St.</a>'
        ]
        
        print("Testing URL extraction:")
        for i, sample in enumerate(test_samples, 1):
            extracted = extract_waze_url(sample)
            print(f"\nTest {i}:")
            print(f"  Original: {sample[:80]}...")
            print(f"  Extracted: {extracted}")
        return
    
    if not args.input_file:
        parser.error("input_file is required when not using --test")
    
    # Process the CSV file
    process_csv_file(args.input_file, args.output)


if __name__ == "__main__":
    main()

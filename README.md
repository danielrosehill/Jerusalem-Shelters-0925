# Jerusalem Public Shelter Dataset - September 2025

This repository contains updated location data for public shelters in the Jerusalem area, populated on September 19th, 2025. The data has been processed and enhanced to support individual preparedness efforts and geolocation applications.

## Data Source

The original data was provided by the Jerusalem Municipality and is available in the `source_data` folder. This dataset represents the most current information available as of September 19th, 2025.

## Repository Structure

```
├── source_data/
│   └── raw.csv                    # Original data from Jerusalem Municipality
├── cleaned_data/
│   └── light_edits.csv           # Processed data with header normalization
├── geojson/
│   └── jerusalem_shelters.geojson # GeoJSON format for mapping applications
├── scripts/
│   ├── strip_waze_link.py        # Script for extracting Waze navigation links
│   └── validate_geojson.py       # GeoJSON validation utility
└── extract_waze_links.py         # Main data processing script
```

## Data Processing

The following enhancements have been applied to the original municipal data:

1. **Waze Link Extraction**: Navigation links have been extracted and processed for easier programmatic access
2. **Header Normalization**: Column headers have been standardized for consistency
3. **GeoJSON Conversion**: Data has been converted to GeoJSON format for use in mapping applications and geolocation services

## Intended Use

This dataset is provided to assist with:

- **Individual Preparedness**: Citizens can access current shelter location information for emergency planning
- **Geolocation Applications**: The processed data supports mapping and navigation applications
- **Personal Use**: The data has been formatted for integration into personal emergency preparedness tools

## Data Format

- **CSV Format**: Available in both raw and cleaned versions
- **GeoJSON Format**: Suitable for web mapping applications, GIS software, and location-based services
- **Coordinate System**: Standard latitude/longitude coordinates for universal compatibility

## Usage Notes

- Data is current as of September 19th, 2025
- Users should verify shelter availability and accessibility during actual emergency situations
- This data is intended to supplement, not replace, official emergency communications

## Scripts

The repository includes utility scripts for data processing and validation:

- `extract_waze_links.py`: Main processing script for data enhancement
- `scripts/strip_waze_link.py`: Utility for Waze link extraction
- `scripts/validate_geojson.py`: GeoJSON format validation

---

*This dataset is provided for public safety and preparedness purposes. Always follow official emergency guidance and communications during actual emergency situations.*

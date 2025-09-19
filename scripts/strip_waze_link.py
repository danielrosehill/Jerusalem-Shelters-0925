#!/usr/bin/env python3
import csv
import html
import os
import re
import sys
from tempfile import NamedTemporaryFile


HREF_RE = re.compile(r'href\s*=\s*"([^"]+)"', re.IGNORECASE)


def extract_waze_url(value: str) -> str:
    if not value:
        return value
    s = value.strip()
    # If already a plain URL, return as-is
    if s.lower().startswith(("http://", "https://")) and "<" not in s and ">" not in s:
        return s
    # Try to extract from href
    m = HREF_RE.search(s)
    if m:
        return html.unescape(m.group(1)).strip()
    # Fallback: find first http(s) substring
    idx = s.find("http://")
    if idx == -1:
        idx = s.find("https://")
    if idx != -1:
        # take until a quote, space, or tag close
        end = len(s)
        for stopper in ['"', "'", ">", "<", " "]:
            j = s.find(stopper, idx + 1)
            if j != -1:
                end = min(end, j)
        return html.unescape(s[idx:end]).strip()
    return s


def process_csv(path: str, column: str = "waze_link") -> None:
    # Read and rewrite atomically with a backup
    tmp_fd = None
    tmp_path = None
    with open(path, "r", encoding="utf-8-sig", newline="") as rf:
        reader = csv.DictReader(rf)
        fieldnames = reader.fieldnames
        if not fieldnames:
            raise SystemExit("CSV has no header row")
        if column not in fieldnames:
            raise SystemExit(f"Column '{column}' not found. Columns: {fieldnames}")

        # Create temp file in same directory to avoid cross-device issues
        target_dir = os.path.dirname(os.path.abspath(path)) or "."
        tf = NamedTemporaryFile(
            "w",
            delete=False,
            encoding="utf-8",
            newline="",
            dir=target_dir,
            prefix=os.path.basename(path) + ".tmp.",
        )
        tmp_fd = tf
        tmp_path = tf.name
        writer = csv.DictWriter(tf, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            orig = row.get(column, "")
            row[column] = extract_waze_url(orig)
            writer.writerow(row)
        tf.close()

    # Backup original, then replace
    backup_path = path + ".bak"
    if os.path.exists(backup_path):
        os.remove(backup_path)
    os.replace(path, backup_path)
    os.replace(tmp_path, path)
    print(f"Updated '{path}'. Backup saved to '{backup_path}'.")


def main(argv: list[str]) -> int:
    import argparse
    p = argparse.ArgumentParser(description="Replace HTML waze links with direct URLs in a CSV.")
    p.add_argument("csv", nargs="?", default="light-edit.csv", help="Path to CSV (default: light-edit.csv)")
    p.add_argument("--column", default="waze_link", help="Column name containing the Waze link")
    args = p.parse_args(argv)

    process_csv(args.csv, args.column)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

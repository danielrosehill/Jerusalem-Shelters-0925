# Jerusalem Public Shelter Dataset - September 2025

![Dataset](https://img.shields.io/badge/Dataset-Public%20Shelters-blue?style=flat-square&logo=database)
![Emergency Preparedness](https://img.shields.io/badge/Emergency-Preparedness-red?style=flat-square&logo=shield)
![Data Format](https://img.shields.io/badge/Format-CSV%20%7C%20GeoJSON-green?style=flat-square&logo=json)
![Last Updated](https://img.shields.io/badge/Updated-September%202025-orange?style=flat-square&logo=calendar)
![Location](https://img.shields.io/badge/Location-Jerusalem-purple?style=flat-square&logo=map-pin)

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
 
---

*This dataset is provided for public safety and preparedness purposes. Always follow official emergency guidance and communications during actual emergency situations.*

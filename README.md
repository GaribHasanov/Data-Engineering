# Public Books Dataset - Comprehensive Data Cleansing
This repository contains a data cleansing project focused on improving the quality and consistency of a public books dataset. The dataset initially contained numerous instances of dirty data, including unnecessary symbols, inconsistent city and country names, and entries in various languages.

## Key Steps in the Data Cleansing Process:
Comprehensive Data Review: Conducted an extensive review of all columns within the dataset to identify and address issues such as unnecessary symbols, irregular formatting, and inconsistent data entries.

### Place of Publication Cleansing:

Identified and corrected entries in the "Place of Publication" column, which included city and country names with unnecessary symbols and foreign language entries (e.g., "ZuÌˆrich," "'s Gravenhage").
Downloaded a standardized list of city names in English and saved it to an Excel file.
Translated the existing "Place of Publication" entries to English and matched them against the downloaded list.
Cleaned matched entries and applied necessary transformations to unmatched rows, ensuring all place names were consistent and in English.
Transformation of Unmatched Data: For rows that did not match the standardized list, further data transformations were performed to correct and standardize these entries.

## Outcome:
The result is a cleansed dataset with all columns standardized, free of unnecessary symbols, and with consistent place names in English. This project exemplifies thorough data cleaning techniques applied to a complex, real-world dataset.

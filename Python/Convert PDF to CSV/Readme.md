# PPNC PDF to CSV Converter

A Python script that converts daily fuel price PDFs from the Petrol Price Notification Centre into a structured CSV format. This tool extracts petrol and diesel prices for major metropolitan cities in India (Mumbai, Delhi, Chennai, and Kolkata).

## Features

- Extracts fuel prices from PPNC PDF documents
- Processes both petrol and diesel prices
- Covers major metropolitan cities: Mumbai, Delhi, Chennai, and Kolkata
- Converts data into a structured CSV format with date indexing
- Handles the specific format of PPNC price notification PDFs

## Datasets Used
fuel_prices_metro_cities.csv -> Created with the data pdf from 2017 to 2024 got from the PPAC website

Link :- https://ppac.gov.in/retail-selling-price-rsp-of-petrol-diesel-and-domestic-lpg/rsp-of-petrol-and-diesel-in-metro-cities-since-16-6-2017


## Prerequisites

- Python 3.x
- Required Python packages:
  - PyPDF2
  - pandas
  - re (Regular Expressions, included in Python standard library)

`pip install PyPDF2 pandas`

## Thought Process
*"I can't find a proper dataset for the Historic Prices of Petrol and Diesel, let me create my own"*

from PyPDF2 import PdfReader
import re

# Load the PDF
pdf_path = 'data/1732854044_PP_9_a_DailyPriceMSHSD_Metro_29.11.2024.pdf'  #Input the path to the PDF downloaded from PPNC Website
reader = PdfReader(pdf_path)

# Extract text from all pages
text = ""
for page in reader.pages:
    text += page.extract_text()

# Extract data using regular expressions
# Pattern: Date followed by petrol and diesel prices for Mumbai, Delhi, Chennai, and Kolkata
pattern = re.compile(
    r'(\d{2}-[A-Za-z]{3}-\d{2})\s+'  # Date
    r'([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+'  # Petrol prices for cities
    r'\1\s+'  # Repeated date for diesel prices
    r'([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)'  # Diesel prices for cities
)

matches = pattern.findall(text)

# Prepare the extracted data into a structured format
columns = [
    "date of revision",
    "Petrol Price in Mumbai", "Diesel Price in Mumbai",
    "Petrol Price in Delhi", "Diesel Price in Delhi",
    "Petrol Price in Chennai", "Diesel Price in Chennai",
    "Petrol Price in Kolkata", "Diesel Price in Kolkata"
]

data = []
for match in matches:
    date, pm, pd, pc, pk, dm, dd, dc, dk = match
    data.append([date, float(pm), float(dm), float(pd), float(dd), float(pc), float(dc), float(pk), float(dk)])

# Define the column names
columns = [
    "date_of_revision",
    "Petrol_Price_in_Mumbai", "Diesel_Price_in_Mumbai",
    "Petrol_Price_in_Delhi", "Diesel_Price_in_Delhi",
    "Petrol_Price_in_Chennai", "Diesel_Price_in_Chennai",
    "Petrol_Price_in_Kolkata", "Diesel_Price_in_Kolkata"
]

import pandas as pd

# Create a DataFrame
df = pd.DataFrame(data, columns=columns)

# Save the DataFrame to a CSV file
output_path = 'fuel_prices_metro_cities.csv'
df.to_csv(output_path, index=False)

print(f"Data successfully saved to {output_path}")
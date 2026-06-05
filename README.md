# PDF to Excel Extractor

A Python tool to extract data from PDF invoices and export to Excel automatically.

## What It Does

- Reads multiple PDF invoice files
- Extracts key information: Invoice Number, Date, Customer Name, Total Amount
- Exports all data to a clean Excel file

## Technologies Used

- Python
- pdfplumber (PDF text extraction)
- pandas (data manipulation)
- openpyxl (Excel export)

## Project Structure

pdf-to-excel-extractor/
├── samples_invoices/     # Folder containing PDF files
│   ├── Invoice_001.pdf
│   ├── Invoice_002.pdf
│   └── ...
├── pdf_to_excel.py       # Main script
├── requirements.txt      # Python dependencies
├── hasil_invoices.xlsx   # Output file (generated)
└── README.md

## How to Run

### 1. Install dependencies

pip install -r requirements.txt

### 2. Place your PDF files

Put your PDF invoices inside the samples_invoices/ folder

### 3. Run the script

python pdf_to_excel.py

### 4. Check the output

Open hasil_invoices.xlsx to see the extracted data

## Sample Output

| filename | invoice_no | date | customer | total |
|----------|-----------|------|----------|-------|
| Invoice_001.pdf | INV-001 | 2025-06-01 | John Doe | 150.0 |
| Invoice_002.pdf | INV-002 | 2025-06-02 | Jane Smith | 200.0 |
| Invoice_003.pdf | INV-003 | 2025-06-03 | Bob Johnson | 75.5 |

## Features

- Batch processing (handle multiple PDFs at once)
- Regex-based data extraction (customizable)
- Automatic Excel export
- Error handling for missing or corrupted files

## Business Value

- Time saved: 2 hours of manual data entry reduced to 5 seconds
- Accuracy: 100% extraction (verified manually)
- Scalable: Works with 5 or 500+ PDF files

## Customization

To adapt to your PDF format, modify the regex patterns in pdf_to_excel.py:

invoice_no = re.search(r"Invoice No[:\s]+(\S+)", text, re.IGNORECASE)
date = re.search(r"Date[:\s]+(\d{4}-\d{2}-\d{2})", text, re.IGNORECASE)
customer = re.search(r"Customer[:\s]+(.+)", text, re.IGNORECASE)
total = re.search(r"Total[:\s]*\$?([\d,]+\.?\d*)", text, re.IGNORECASE)

# Preview in Picture
1. shot from Terminal in Visual Studio Code
<img width="434" height="135" alt="image" src="https://github.com/user-attachments/assets/c3a40303-fe2f-4b76-891f-b85702824173" />

2. Invoices result in Excel
<img width="403" height="224" alt="image" src="https://github.com/user-attachments/assets/5094ba2c-1507-4c3f-b609-163ded0aafeb" />

## Requirements

- Python 3.12.1
- Libraries: pdfplumber, pandas, openpyxl
- Visual Studio Codes

## Author

Fairuz Fernanda 

## Related Projects

- Customer Churn Prediction: https://github.com/FairuzFernanda30/churn-app

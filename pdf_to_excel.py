import pdfplumber
import pandas as pd
import os
import re

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# PDF folder relative to script location
folder_path = os.path.join(script_dir, "samples_invoices")

print(f"📁 Looking for PDFs in: {folder_path}")

# Check if folder exists
if not os.path.exists(folder_path):
    print(f"❌ Folder '{folder_path}' not found!")
    print("📌 Make sure the 'samples_invoices' folder exists in the same location as this script.")
    exit()

# List to store all extracted data
all_data = []

print("🔄 Processing PDF files...")

# Loop through all PDF files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
        file_path = os.path.join(folder_path, filename)
        
        try:
            # Open PDF with pdfplumber
            with pdfplumber.open(file_path) as pdf:
                # Get the first page
                first_page = pdf.pages[0]
                
                # Extract text
                text = first_page.extract_text()
                
                # Parse data from text using regex
                # Adjust these patterns to match your PDF format
                invoice_no = re.search(r"Invoice No[:\s]+(\S+)", text, re.IGNORECASE)
                date = re.search(r"Date[:\s]+(\d{4}-\d{2}-\d{2})", text, re.IGNORECASE)
                customer = re.search(r"Customer[:\s]+(.+)", text, re.IGNORECASE)
                total = re.search(r"Total[:\s]*\$?([\d,]+\.?\d*)", text, re.IGNORECASE)
                
                # Save to dictionary
                data = {
                    "filename": filename,
                    "invoice_no": invoice_no.group(1) if invoice_no else "Not found",
                    "date": date.group(1) if date else "Not found",
                    "customer": customer.group(1).strip() if customer else "Not found",
                    "total": float(total.group(1).replace(",", "")) if total else 0
                }
                
                all_data.append(data)
                print(f"✅ {filename} - Invoice: {data['invoice_no']}")
                
        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")

# Convert to DataFrame
if all_data:
    df = pd.DataFrame(all_data)
    
    # Export to Excel
    output_file = "hasil_invoices.xlsx"
    df.to_excel(output_file, index=False)
    
    print(f"\n✅ Done! {len(all_data)} files successfully processed.")
    print(f"📁 Output saved to: {output_file}")
    
    # Display preview of results
    print("\n📊 Preview of results:")
    print(df.to_string(index=False))
else:
    print("\n❌ No PDF files processed. Check the 'samples_invoices' folder.")
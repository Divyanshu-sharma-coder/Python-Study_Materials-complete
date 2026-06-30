import os
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def create_image_watermark(image_path, temp_pdf_path="temp_watermark.pdf"):
    """Creates a temporary single-page PDF containing the image at the bottom-right corner."""
    # Standard letter size is 612 x 792 points. A4 is 595 x 842 points.
    page_width, page_height = letter 
    
    c = canvas.Canvas(temp_pdf_path, pagesize=(page_width, page_height))
    
    # Set watermark image dimensions
    img_width = 60
    img_height = 60
    
    # Calculate bottom-right positioning with a 20-point margin from edges
    x_pos = page_width - img_width - 20
    y_pos = 20
    
    # Draw the image onto the canvas
    c.drawImage(image_path, x_pos, y_pos, width=img_width, height=img_height, mask='auto')
    c.save()

def merge_and_watermark_pdfs(pdf_list, image_path, output_path):
    """Merges PDFs and applies the bottom-right image watermark to every page."""
    # Step 1: Create the temporary watermark layer
    temp_watermark = "temp_watermark.pdf"
    create_image_watermark(image_path, temp_watermark)
    watermark_reader = PdfReader(temp_watermark)
    watermark_page = watermark_reader.pages[0]
    
    writer = PdfWriter()
    
    # Step 2: Read, merge, and stamp each page
    for pdf_path in pdf_list:
        if not os.path.exists(pdf_path):
            print(f"Skipping missing file: {pdf_path}")
            continue
            
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            # merge_page puts the watermark on top. Change over=False if you want it underneath text.
            page.merge_page(watermark_page, over=True)
            writer.add_page(page)
            
    # Step 3: Write final output and clean up
    with open(output_path, "wb") as out_file:
        writer.write(out_file)
        
    writer.close()
    if os.path.exists(temp_watermark):
        os.remove(temp_watermark)
    print(f"Success! Watermarked PDF saved as: {output_path}")

# ==================== CONFIGURATION ====================

# 1. Path to your Github image based on your File Explorer path
watermark_image_path = r"C:\Users\hp\Desktop\Python-series\Projects\Assets\Github.png"

# 2. Your list of source handbooks
source_pdfs = [
    r"C:\Users\hp\Desktop\Python-series\Study Materials\MongoDB Handbook.pdf",
    r"C:\Users\hp\Desktop\Python-series\Study Materials\MYSQL Handbook.pdf",
    r"C:\Users\hp\Desktop\Python-series\Study Materials\The Ultimate HTML handbook.pdf",
    r"C:\Users\hp\Desktop\Python-series\Study Materials\The Ultimate Python Handbook.pdf"
]

# 3. Final execution output path
final_output = "out-watermarked-handbooks.pdf"

merge_and_watermark_pdfs(source_pdfs, watermark_image_path, final_output)

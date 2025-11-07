from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def images_to_pdf(image_folder, output_pdf):
    # Get list of image files in the folder
    image_files = [f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
    image_files.sort()  # Sort to ensure the order is consistent

    # Create a PDF canvas
    c = canvas.Canvas(output_pdf, pagesize=letter)
    width, height = letter

    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        # Open the image using Pillow
        img = Image.open(image_path)
        img_width, img_height = img.size

        # Calculate the position and size to maintain aspect ratio
        aspect = img_width / float(img_height)
        if aspect > 1:
            img_width = width
            img_height = width / aspect
        else:
            img_height = height
            img_width = height * aspect

        x = (width - img_width) / 2
        y = (height - img_height) / 2

        # Draw the image on the PDF
        c.drawImage(image_path, x, y, img_width, img_height)
        c.showPage()  # Create a new page for the next image

    # Save the PDF
    c.save()
    print(f"PDF saved as {output_pdf}")

# Example usage
image_folder = r'C:\Example'
output_pdf = 'output.pdf'
images_to_pdf(image_folder, output_pdf)

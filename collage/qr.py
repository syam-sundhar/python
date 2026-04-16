import qrcode
import os

def generate_qr_code(url, filename="website_qr_code.png"):
    """
    Generates and saves a QR code for a given URL.

    Args:
        url (str): The website URL to encode.
        filename (str): The name of the output image file (must end with .png).
    """
    try:
        # Create a QR code object
        # The make() function is a shortcut for the QRCode class
        img = qrcode.make(url)

        # Save the image to a file
        img.save(filename)

        print(f"QR code successfully generated and saved as '{filename}'")
        print(f"File location: {os.path.abspath(filename)}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
website_link = "https://sahaya-ai-gilt.vercel.app"
generate_qr_code(website_link,"sahaya_ai_qr_code.png")
# Barcode & QR Code Generator

![Demo](https://via.placeholder.com/800x400.png?text=Barcode+%26+QR+Code+Generator+Demo)

A Streamlit web application for generating barcodes and QR codes with customizable options.

## Features
- Generate common barcode formats (Code 128, EAN13, EAN8, UPC-A)
- Create customizable QR codes with color options
- Download generated images in PNG format
- Responsive web interface

## Installation

1. **Clone the repository**  
2. **Navigate to project directory**  
3. **Install dependencies**  

## Usage
1. **Run the application**  
2. **Choose code type**  
- Select either **Barcode** or **QR Code** using the radio buttons
3. **Generate Barcode**  
- Enter the data to encode
- Select barcode type from dropdown
- Click "Generate Barcode"
- Download using the download button
4. **Generate QR Code**  
- Enter text/URL to encode
- Customize colors using sidebar pickers
- Click "Create My QR"
- Download using the download button

## Deployment

Deploy to Streamlit Community Cloud:

1. Create a new app in [Streamlit Community Cloud](https://share.streamlit.io/)
2. Connect your GitHub repository
3. Set main file path to `app.py`
4. Click **Deploy**

[![Deploy](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io/cloud)

## Technologies Used
- Python 3.9+
- Streamlit
- python-barcode
- qrcode

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

import streamlit as st
import barcode
from barcode.writer import ImageWriter
import qrcode
from io import BytesIO
import re

def sanitize_input(input_string, max_length=100):
    sanitized = re.sub(r'[<>&\'"()]', '', str(input_string))
    return sanitized[:max_length]

def validate_barcode_type(barcode_type):
    valid_types = ["code128", "ean13", "ean8", "upca"]
    if barcode_type in valid_types:
        return barcode_type
    return "code128"

def validate_color(color):
    if re.match(r'^#(?:[0-9a-fA-F]{3}){1,2}$', color):
        return color
    return "#000000"

def genbar(data, barcode_type):
    barcode_class = barcode.get_barcode_class(barcode_type)
    barcode_instance = barcode_class(data, writer=ImageWriter())
    buffer = BytesIO()
    barcode_instance.write(buffer)
    buffer.seek(0)
    return buffer

def make_qr(text, color, bg):
    qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=12, border=5)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color=color, back_color=bg)
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer

st.set_page_config(page_title="Code Generator", page_icon="🚀")
st.title("Barcode and QR Code Generator 🚀")
code_type = st.radio("Select code type:", ["Barcode", "QR Code"])

if code_type == "Barcode":
    data_input = st.text_input("Enter the data for the barcode:")
    sanitized_data = sanitize_input(data_input)
    selected_barcode_type = st.selectbox("Select barcode type:", ["code128", "ean13", "ean8", "upca"])
    validated_barcode_type = validate_barcode_type(selected_barcode_type)
    if st.button("Generate Barcode"):
        if sanitized_data:
            try:
                barcode_image = genbar(sanitized_data, validated_barcode_type)
                st.image(barcode_image, caption="Generated Barcode", use_column_width=True)
                st.download_button(label="Download Barcode", data=barcode_image.getvalue(), file_name="barcode.png", mime="image/png")
            except:
                st.error("An error occurred while generating the barcode. Please try again.")
        else:
            st.warning("Please enter valid data for the barcode.")
else:
    st.sidebar.header("QR Settings")
    text_input = st.text_input("Enter: your own Text/Any website Link OR Anything You Like")
    sanitized_text = sanitize_input(text_input)
    color_input = st.sidebar.color_picker("QR Color", value="#000000")
    bg_input = st.sidebar.color_picker("Background", value="#FFFFFF")
    validated_color = validate_color(color_input)
    validated_bg = validate_color(bg_input)
    if st.button("Create My QR"):
        if sanitized_text:
            try:
                qr = make_qr(sanitized_text, validated_color, validated_bg)
                st.image(qr, caption="Your QR", use_column_width=True)
                st.download_button(label="Download QR", data=qr, file_name="qr.png", mime="image/png")
            except:
                st.error("An error occurred while generating the QR code. Please try again.")
        else:
            st.warning("Enter text for the QR code.")

st.sidebar.markdown("---")
st.sidebar.markdown("© 2025 QR & BARCODE Generator")
st.markdown("---")
st.markdown("Made with ❤️ by Ut ©2025")

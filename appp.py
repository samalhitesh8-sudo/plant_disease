import streamlit as st
import base64

# Function to read the HTML file and serve it
def show_html_file(file_path):
    with open(file_path, "r") as f:
        html_code = f.read()

    # The HTML needs to be encoded in base64 to be served securely
    b64_html = base64.b64encode(html_code.encode()).decode()
    st.markdown(f'<iframe src="data:text/html;base64,{b64_html}" style="width:100%; height:800px; border:none;"></iframe>', unsafe_allow_html=True)

# Set up the Streamlit page
st.set_page_config(
    page_title="Plant Disease Detector",
    layout="wide",
)

# Display the HTML file
show_html_file("index.html")
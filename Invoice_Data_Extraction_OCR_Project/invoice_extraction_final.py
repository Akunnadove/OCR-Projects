import base64
import streamlit as st
import pytesseract
import PIL.Image

# Set page config
st.set_page_config(page_title="My Streamlit App", page_icon="::", layout="wide", initial_sidebar_state="expanded")

@st.experimental_memo
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("download.jpg")
imgs = get_img_as_base64("photo.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{imgs}");
background-size: cover;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-size: cover;
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}

#extractor-header {{
    color: white; 
  }}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
#st.sidebar.header("Extractor Version.0 ")

st.sidebar.markdown(f'<h1 id="extractor-header">Data Extractor Version 1.0 </h1>', unsafe_allow_html=True)

# Configuration for pytesseract
myconfig = r"--psm 11 --oem 3"

# Function to process image 1
def process_image_1():
    text1 = pytesseract.image_to_string(PIL.Image.open("C:/Users/Akunna Anyamkpa/Downloads/Invoice 1.png"), config=myconfig)
    image1_list = text1.split('\n\n')
    total_amount_due = image1_list[28].split(' ')[-1]
    image1_dict = {
        'Date Issued': image1_list[1],
        'Items': [image1_list[11], image1_list[14], image1_list[17]],
        'Total Amount Due': '$ ' + total_amount_due
    }
    return image1_dict

# Function to process image 2
def process_image_2():
    text2 = pytesseract.image_to_string(PIL.Image.open("C:/Users/Akunna Anyamkpa/Downloads/Invoice 2.png"), config=myconfig)
    image2_list = text2.split('\n\n')
    total_amount_due = image2_list[48].strip()
    image2_dict = {
        'Date Issued': '2018-09-25',
        'Items': [image2_list[29], image2_list[35], image2_list[37]],
        'Total Amount Due': '$' + total_amount_due
    }
    return image2_dict

# Function to process image 3
def process_image_3():
    text3 = pytesseract.image_to_string(PIL.Image.open("C:/Users/Akunna Anyamkpa/Downloads/Invoice 3.jpg"), config=myconfig)
    image3_list = text3.split('\n\n')
    total_amount_due = image3_list[68].strip()
    image3_dict = {
        'Date Issued': '12/23',
        'Items': [image3_list[29], image3_list[35], image3_list[40], image3_list[46]],
        'Total Amount Due': total_amount_due
    }
    return image3_dict

# Streamlit app
def main():
    st.title("Invoice Data Extraction")
    
    # Display images and buttons in a horizontal layout
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Image 1:")
        st.image("C:/Users/Akunna Anyamkpa/Downloads/Invoice 1.png", use_column_width=True)
        if st.button("Extract data from Image 1"):
            image_data = process_image_1()
            st.write("Data Extracted from Image 1:")
            st.write(image_data)
            st.write("Image processing completed.")
    
    with col2:
        st.subheader("Image 2:")
        st.image("C:/Users/Akunna Anyamkpa/Downloads/Invoice 2.png", use_column_width=True)
        if st.button("Extract data from Image 2"):
            image_data = process_image_2()
            st.write("Data Extracted from Image 2:")
            st.write(image_data)
            st.write("Image processing completed.")
    
    with col3:
        st.subheader("Image 3:")
        st.image("C:/Users/Akunna Anyamkpa/Downloads/Invoice 3.jpg", use_column_width=True)
        if st.button("Extract data from Image 3"):
            image_data = process_image_3()
            st.write("Data Extracted from Image 3:")
            st.write(image_data)
            st.write("Image processing completed.")

if __name__ == "__main__":
    main()

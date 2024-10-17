import streamlit as st 
import os 
import google.generativeai as genai
import PIL.Image

#Function to get the GeminiAI response
def get_gemini_response(api_key , prompt , image):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash-002")
    response = model.generate_content([prompt,image])
    return response.text

#Initialize the Streamlit App
st.set_page_config(page_title="Image Analyzer")

st.header("Visual Application")

#Input field for the Google API Key
api_key = st.text_input("Enter your Gemini API Key: ",type="password")

#Input prompt from the user 
prompt = st.text_input ("Input Prompt (e.g., 'What is this photo?'):", key="input")

#File uploader to allow the user to upload an Image
Uploaded_file = st.file_uploader("Chose an image...", type=["jpg", "jpeg" ,"png"])
image = None

if Uploaded_file is not None:
    image=PIL.Image.open(Uploaded_file)
    st.image(image, caption="Uploaded Image" , use_column_width=True)

#Button to submit the request
submit = st.button("Analyze the image")

#If the submit button is clicked, configure the Api key and get the Gemini AI response
if submit and api_key and image is not None:
   try:
       response = get_gemini_response(api_key,prompt, image)
       st.subheader("The Response is:")
       st.write(response)
   except Exception as e:
       st.error(f"An error occurred: {e}")
       


#import necessary modules
import streamlit as st
from pathlib import Path
import google.generativeai as genai

from api_key import api_key

#configure genai with api key
genai.configure(api_key=api_key)
#set up the model
generation_config = {
    "temperature" : 0.4,
    "top_p" : 1,
    "top_k" : 32,
    "max_output_tokens" : 4096,
}

#apply safety settings
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
]

system_prompt = """
As a highly skilled medical practitioner specializing in image analysis, you are tasked with examining medical images for a renowned hospital. Your expertise is crucial in identifying any anomalies, diseases, or health issues that may be present in the images.

Your Responsibilities include:

1. Detailed Analysis: Thoroughly analyze each image, focusing on identifying any abnormal findings.
2. Findings Report: Document all observed anomalies or signs of disease. Clearly articulate these findings in a structured format.
3. Recommendations and Next Steps: Based on your analysis, suggest potential next steps, including further tests or treatments as applicable.
4. Treatment Suggestions: If appropriate, recommend possible treatment options or interventions

Important Notes:

1. Scope of Response: Only respond if the image pertains to human health issues.
2. Clarity of Image: In cases where the image quality impedes clear analysis, note that certain aspects are "Unable to be determined based on the provided image.
3. Disclaimer: Accompany your analysis with the disclaimer: "Consult with a Doctor before making any decisions."
Settings

4. Your insights are invaluable in guiding clinical decisions. Please proceed with the analysis, adhering to the structured approach outlined above



"""
#model configuration
model = genai.GenerativeModel(model_name="gemini-2.5-pro",
                              generation_config=generation_config,
                                safety_settings=safety_settings)


# Set the page confirmation

st.set_page_config(page_title="VitalImage Analytics", page_icon=":robot", layout="wide")

#set the logo
st.image(r"C:\Users\ashir\Pictures\download.png", width=200)

#set the title
st.markdown("<h1 style='text-align: center; color: #00BFFF;'>Vital Image Analytics</h1>", unsafe_allow_html=True)

# Set the subtitle

st.markdown("<h3 style='text-align: center;'>An application that can help users to identify medical images</h3>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload the medical image for analysis", type=["jpg", "jpeg", "png"])
if uploaded_file:
    st.image(uploaded_file, width=300, caption="Uploaded Medical Image")
submit_button = st.button("Generate the Analysis")

if submit_button:
    #process the uploaded image
    image_data = uploaded_file.getvalue()

    #making our image ready
    image_parts = [
        {
            "mime_type": "image/jpeg",
            "data": image_data,
        },
    ]
    #making our prompt ready
    prompt_parts = [
        
        image_parts[0],
        system_prompt,
    ]
    #generate the response based on prompt and image
    response = model.generate_content(prompt_parts)
    if response:
        st.markdown("<h2 style='text-align: center;'>Here is the analysis based on your image:</h2>", unsafe_allow_html=True)
        st.markdown(f"<div style='text-align: justify;'>{response.text}</div>", unsafe_allow_html=True)
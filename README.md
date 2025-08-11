# Medical-Analysis-Project
📂 Project Structure
app.py
The main application script.
-Built using Streamlit for an interactive web interface.
-Integrates Google Generative AI (Gemini 2.5 Pro) for medical image analysis.
-Allows users to upload medical images (.jpg, .jpeg, .png) and receive detailed AI-generated reports.
-Implements safety settings to block harmful or inappropriate outputs.
-Uses a structured medical analysis prompt, providing findings, recommendations, and a disclaimer.

api_key.py
-Contains the Google Generative AI API key as a variable (api_key).
-Important: For security, this file should be excluded from version control by adding it to .gitignore.
-Used in app.py to authenticate API calls to the Gemini model.

api_key.cpython-311.pyc
-Compiled Python bytecode version of api_key.py.
-Automatically generated when running the application.
-Not required for editing or version control—safe to ignore in .gitignore.

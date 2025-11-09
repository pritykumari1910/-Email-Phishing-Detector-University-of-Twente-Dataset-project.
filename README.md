<img width="1885" height="795" alt="image" src="https://github.com/user-attachments/assets/dd1759ff-6914-4e1d-9ad1-ad3e2d4ca6ca" />


📌 Overview

The Email Phishing Detector is an AI-powered web app that classifies email messages as Phishing or Legitimate using Natural Language Processing (NLP) and Machine Learning.
It’s trained on the University of Twente’s Phishing Validation Emails Dataset, which includes 2,000 real and synthetic emails labeled as phishing or safe.

The web interface is built with Streamlit, offering a modern design, animated gradient header, and dark/light themes for better user experience.

🧠 Tech Stack

Programming Language: Python

Framework: Streamlit

Machine Learning: Scikit-learn (TF-IDF + Logistic Regression)

Model Storage: Joblib

Libraries Used:

pandas

numpy

scikit-learn

streamlit

joblib

re, string (for text preprocessing)

📊 Dataset

Name: Phishing Validation Emails Dataset

Source: University of Twente Research Repository

Records: 2,000 emails (Phishing + Legitimate)

Description: Contains text and metadata from emails labeled as either phishing or safe for research and model training.

🚀 Features

✅ Detects Phishing or Legitimate emails using NLP
✅ Streamlit UI with animated gradient header
✅ Dark / Light Mode Toggle
✅ Shows word count for entered text
✅ Uses TF-IDF + Logistic Regression
✅ Fast and lightweight deployment

🧩 Project Workflow

Data Cleaning & Preprocessing

Lowercasing

Removing links, emails, digits, and punctuation

Token normalization

Feature Extraction

Convert cleaned text to numeric features using TF-IDF

Model Training

Train a Logistic Regression classifier on labeled data

Deployment

Save trained model using joblib

Create web UI in Streamlit

📂 Folder Structure
email-phishing-detector/
│
├── app.py
├── models/
│   └── phishing_detector_utwente.joblib
├── data/
│   └── phishing_validation_emails.csv
├── phishing_detector.ipynb
├── requirements.txt
└── README.md

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/email-phishing-detector.git
cd email-phishing-detector

2️⃣ Install Dependencies
pip install -r requirements.txt


Example requirements.txt:

streamlit
scikit-learn
pandas
numpy
joblib

3️⃣ Add Dataset

Download the dataset from
📎 University of Twente Research Repository

and save it to:

data/phishing_validation_emails.csv

4️⃣ Run the App Locally
streamlit run app.py

💻 Example Usage

Input Example:

Your bank account has been suspended. Please click here to verify your information immediately.


Output Example:

🚨 Phishing Email Detected!



🌈 User Interface

✨ Modern UI built with Streamlit
🌙 Dark/Light mode toggle
🎨 Animated gradient header
💌 Responsive design for better readability

📈 Model Evaluation
Metric	Score
Accuracy	95.8%
Precision	95%
Recall	96%
F1 Score	95%

(Performance may vary depending on dataset split and preprocessing.)

💡 Future Improvements

Integrate Transformer models (BERT) for deeper NLP understanding

Add email header analysis and URL inspection

Deploy using Streamlit Cloud or Hugging Face Spaces

Develop an API backend with FastAPI or Flask

🧾 Credits

Dataset: University of Twente — Phishing Validation Emails Dataset

Model: TF-IDF + Logistic Regression (Scikit-learn)

UI Framework: Streamlit

Developer: Prity Kumari 👩‍💻

📜 License

This project is licensed under the MIT License — feel free to use and modify with attribution.

🌐 Connect

⭐ If you found this helpful, give it a Star on GitHub!
💬 Feedback or collaboration ideas? Reach out anytime.

import streamlit as st
import joblib
import re, string

# ===================== CONFIGURATION =====================
st.set_page_config(
    page_title="🕵️ Email Phishing Detector",
    page_icon="📧",
    layout="centered"
)

# ===================== CUSTOM STYLING =====================
st.markdown("""
    <style>
    /* Smooth gradient header */
    .title-container {
        text-align: center;
        padding: 1rem 0 1.5rem 0;
        background: linear-gradient(90deg, #007cf0, #00dfd8, #007cf0);
        background-size: 300% 300%;
        animation: gradientShift 6s ease infinite;
        color: white;
        border-radius: 12px;
        margin-bottom: 1rem;
    }

    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .result-box {
        padding: 1.2rem;
        border-radius: 12px;
        margin-top: 1.5rem;
        font-weight: bold;
        text-align: center;
        font-size: 1.2rem;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }

    .phish {
        background-color: #ffe5e5;
        color: #b80000;
        border: 2px solid #ff4d4d;
    }

    .safe {
        background-color: #e6ffee;
        color: #006622;
        border: 2px solid #00b359;
    }

    /* Dark Mode Styling */
    body.dark {
        background-color: #0E1117;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# ===================== THEME TOGGLE =====================
theme = st.sidebar.radio("🎨 Theme", ["🌞 Light Mode", "🌙 Dark Mode"])
if theme == "🌙 Dark Mode":
    st.markdown("<style>body { background-color: #0E1117; color: #FAFAFA; }</style>", unsafe_allow_html=True)

# ===================== MODEL SETUP =====================
MODEL_PATH = "models/phishing_detector_utwente.joblib"

def clean_text(s):
    s = s.lower()
    s = re.sub(r'https?://\S+|www\.\S+', ' ', s)
    s = re.sub(r'\S+@\S+', ' ', s)
    s = re.sub(r'\d+', ' ', s)
    s = s.translate(str.maketrans('', '', string.punctuation))
    s = re.sub(r'\s+', ' ', s).strip()
    return s

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()

# ===================== HEADER =====================
st.markdown("""
<div class="title-container">
    <h1>🕵️ Email Phishing Detector</h1>
    <p>Detect if an email is <strong>Phishing</strong> or <strong>Legitimate</strong> using NLP & ML</p>
</div>
""", unsafe_allow_html=True)

# ===================== INPUT AREA =====================
st.markdown("### 📧 Paste Email Text Below:")
email_text = st.text_area("", height=250, placeholder="Type or paste email content here...")

if email_text:
    word_count = len(email_text.split())
    st.caption(f"📝 Word Count: {word_count}")

# ===================== PREDICTION =====================
if st.button("🔍 Analyze Email"):
    if email_text.strip() == "":
        st.warning("⚠️ Please enter some email text before detection.")
    else:
        cleaned = clean_text(email_text)
        pred = model.predict([cleaned])[0]

        if pred == 1:
            st.markdown(
                "<div class='result-box phish'>🚨 <strong>Phishing Email Detected!</strong></div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                "<div class='result-box safe'>✅ <strong>Legitimate Email</strong></div>",
                unsafe_allow_html=True
            )

# ===================== SIDEBAR =====================
st.sidebar.title("📊 About Project")
st.sidebar.info("""
**AI Email Phishing Detector**

This app uses NLP with TF-IDF + Logistic Regression  
to classify emails as *phishing* or *legitimate*.

**Dataset:**  
University of Twente — *Phishing Validation Emails* (2000 samples)
""")

st.sidebar.markdown("🔗 [Dataset Link](https://research.utwente.nl/en/datasets/phishing-validation-emails-dataset)")
st.sidebar.markdown("👩‍💻 Developed by *Prity Kumari*")

# ===================== FOOTER =====================
st.markdown("---")
st.markdown("""
💡 **Tip:** Phishing emails often include suspicious links, urgency, or requests for confidential info.  
🧠 *Model trained using TF-IDF + Logistic Regression (University of Twente Dataset).*
""")

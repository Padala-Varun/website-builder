import streamlit as st
from extractor.pdf_loader import extract_text_from_pdf
from generator.site_generator import generate_portfolio_site
import os
import time

# Set Streamlit page config with dark theme
st.set_page_config(
    page_title="Portfolio Builder AI", 
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon="🚀"
)

# Custom CSS for modern UI
st.markdown("""
<style>
    /* Import modern fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    
    /* Root variables */
    :root {
        --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        --success-gradient: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        --dark-bg: #0f1419;
        --card-bg: rgba(255, 255, 255, 0.05);
        --text-primary: #ffffff;
        --text-secondary: #a0a9c0;
        --border-color: rgba(255, 255, 255, 0.1);
    }
    
    /* Main container styling */
    .stApp {
        background: linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 50%, #16213e 100%);
        font-family: 'Inter', sans-serif;
    }
    
    /* Hero section */
    .hero-container {
        text-align: center;
        padding: 4rem 2rem;
        margin-bottom: 3rem;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        border-radius: 20px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        position: relative;
        overflow: hidden;
    }
    
    .hero-container::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(102, 126, 234, 0.1) 0%, transparent 70%);
        animation: pulse 4s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); opacity: 0.5; }
        50% { transform: scale(1.1); opacity: 0.8; }
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        background: var(--primary-gradient);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem;
        position: relative;
        z-index: 1;
    }
    
    .hero-subtitle {
        font-size: 1.3rem;
        color: var(--text-secondary);
        margin-bottom: 2rem;
        font-weight: 400;
        position: relative;
        z-index: 1;
    }
    
    /* Upload section */
    .upload-section {
        background: var(--card-bg);
        border-radius: 16px;
        padding: 2.5rem;
        margin: 2rem 0;
        border: 1px solid var(--border-color);
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }
    
    .upload-section:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(102, 126, 234, 0.2);
    }
    
    /* File uploader styling */
    .stFileUploader > div > div {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        border: 2px dashed rgba(102, 126, 234, 0.5);
        border-radius: 12px;
        padding: 2rem;
        transition: all 0.3s ease;
    }
    
    .stFileUploader > div > div:hover {
        border-color: rgba(102, 126, 234, 0.8);
        background: rgba(102, 126, 234, 0.15);
    }
    
    /* Button styling */
    .stButton > button {
        background: var(--primary-gradient);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.6);
    }
    
    /* Download button */
    .stDownloadButton > button {
        background: var(--success-gradient);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(79, 172, 254, 0.4);
    }
    
    .stDownloadButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(79, 172, 254, 0.6);
    }
    
    /* Success/Info messages */
    .stSuccess {
        background: linear-gradient(135deg, rgba(79, 172, 254, 0.1) 0%, rgba(0, 242, 254, 0.1) 100%);
        border: 1px solid rgba(79, 172, 254, 0.3);
        border-radius: 12px;
        backdrop-filter: blur(10px);
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: var(--card-bg);
        border-radius: 8px;
        border: 1px solid var(--border-color);
    }
    
    /* Spinner customization */
    .stSpinner {
        text-align: center;
    }
    
    /* Progress animation */
    @keyframes slideInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .animated-card {
        animation: slideInUp 0.6s ease-out;
    }
    
    /* Feature cards */
    .feature-card {
        background: var(--card-bg);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid var(--border-color);
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.15);
    }
    
    .feature-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }
    
    .feature-title {
        font-size: 1.2rem;
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: 0.5rem;
    }
    
    .feature-desc {
        color: var(--text-secondary);
        font-size: 0.9rem;
    }
    
    /* Step indicator */
    .step-indicator {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 2rem 0;
    }
    
    .step {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background: var(--card-bg);
        border: 2px solid var(--border-color);
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 1rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .step.active {
        background: var(--primary-gradient);
        border-color: transparent;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    .step-line {
        width: 60px;
        height: 2px;
        background: var(--border-color);
    }
    
    .step-line.active {
        background: var(--primary-gradient);
    }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-container">
    <h1 class="hero-title">🚀 AI Portfolio Builder</h1>
    <p class="hero-subtitle">Transform your resume into a stunning portfolio website in seconds</p>
</div>
""", unsafe_allow_html=True)

# Feature cards
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📄</div>
        <div class="feature-title">Smart PDF Extraction</div>
        <div class="feature-desc">Advanced AI parsing extracts every detail from your resume</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🎨</div>
        <div class="feature-title">Beautiful Design</div>
        <div class="feature-desc">Generate modern, responsive portfolio websites automatically</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">⚡</div>
        <div class="feature-title">Instant Results</div>
        <div class="feature-desc">Get your professional portfolio ready in under 30 seconds</div>
    </div>
    """, unsafe_allow_html=True)

# Step indicator
current_step = 1
st.markdown("""
<div class="step-indicator">
    <div class="step active">1</div>
    <div class="step-line"></div>
    <div class="step">2</div>
    <div class="step-line"></div>
    <div class="step">3</div>
</div>
""", unsafe_allow_html=True)

# Upload section
st.markdown('<div class="upload-section animated-card">', unsafe_allow_html=True)
st.markdown("### 📤 Upload Your Resume")
st.markdown("*Drag and drop your PDF resume below to get started*")

uploaded_file = st.file_uploader(
    "Choose your resume file", 
    type=["pdf"],
    help="Upload a PDF version of your resume for best results"
)
st.markdown('</div>', unsafe_allow_html=True)

# Process uploaded file
if uploaded_file:
    # Update step indicator
    st.markdown("""
    <div class="step-indicator">
        <div class="step active">✓</div>
        <div class="step-line active"></div>
        <div class="step active">2</div>
        <div class="step-line"></div>
        <div class="step">3</div>
    </div>
    """, unsafe_allow_html=True)
    
    with st.spinner("🔍 Analyzing your resume with AI..."):
        # Add a small delay for better UX
        time.sleep(1)
        text = extract_text_from_pdf(uploaded_file)

    st.success("✅ Resume successfully analyzed and processed!")

    # Show extracted text with modern styling
    with st.expander("🔍 View Extracted Content", expanded=False):
        st.markdown(f"""
        <div style="background: var(--card-bg); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color); font-family: 'JetBrains Mono', monospace; font-size: 0.9rem; line-height: 1.6;">
            {text}
        </div>
        """, unsafe_allow_html=True)

    # Generation section
    st.markdown('<div class="upload-section animated-card">', unsafe_allow_html=True)
    st.markdown("### 🎨 Generate Your Portfolio")
    st.markdown("*Click below to create your personalized portfolio website*")
    
    if st.button("🚀 Create My Portfolio Website", key="generate_btn"):
        # Update step indicator
        st.markdown("""
        <div class="step-indicator">
            <div class="step active">✓</div>
            <div class="step-line active"></div>
            <div class="step active">✓</div>
            <div class="step-line active"></div>
            <div class="step active">3</div>
        </div>
        """, unsafe_allow_html=True)
        
        with st.spinner("🧠 AI is crafting your beautiful portfolio..."):
            # Add progress simulation
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.02)
                progress_bar.progress(i + 1)
            
            html_code = generate_portfolio_site(text)

            # Save the generated site
            output_path = "output/site.html"
            os.makedirs("output", exist_ok=True)
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(html_code)

        st.success("🎉 Your stunning portfolio website is ready!")

        # Preview section
        st.markdown("### 👀 Live Preview")
        st.markdown("*Here's how your portfolio will look:*")
        
        # Website preview with better styling
        st.components.v1.html(html_code, height=700, scrolling=True)

        # Download section
        st.markdown("### 📥 Download Your Website")
        with open(output_path, "rb") as f:
            st.download_button(
                "⬇️ Download Portfolio Website",
                f,
                file_name="my_portfolio_website.html",
                mime="text/html",
                help="Download your complete portfolio website as an HTML file"
            )
        
        # Additional options
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 Generate Another Version"):
                st.rerun()
        
        with col2:
            if st.button("✨ Customize Further"):
                st.info("💡 Pro tip: You can edit the downloaded HTML file to customize colors, fonts, and layout!")

    st.markdown('</div>', unsafe_allow_html=True)


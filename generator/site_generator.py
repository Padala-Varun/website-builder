import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def generate_portfolio_site(resume_text: str) -> str:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in .env file")

    # Configure Gemini with AI Studio API Key
    genai.configure(api_key=api_key)

    try:
        # ✅ Use Gemini 1.5 Flash model
        model = genai.GenerativeModel("gemini-2.5-flash")

        prompt = (
    "You are a professional front-end web designer. Based on the resume text below, "
    "generate a stunning, colorful, modern **single-page personal portfolio website** "
    "using HTML, rich inline CSS, and JavaScript — all in one single HTML file.\n\n"
    
    "🎨 Design Style:\n"
    "- Use **vibrant colors**, **gradients**, and **creative backgrounds**\n"
    "- Apply **shadows, border radius, hover effects**\n"
    "- Use elegant, professional **Google Fonts** via `@import`\n"
    "- Add a **full-screen hero section** with background gradient or image\n\n"
    
    
    "📱 Responsive Layout:\n"
    "- Use **Flexbox** or **CSS Grid**\n"
    "- Mobile-friendly with media queries\n\n"

    "🔧 Functionality:\n"
    "- JavaScript for **scroll animations**, **sticky nav**, and **smooth scrolling**\n"
    "- Add reveal-on-scroll effects for each section\n\n"

    "📂 Sections to Include:\n"
    "1. Hero (Name, Role, Tagline)\n"
    "2. About Me\n"
    "3. Skills (with progress bars or badges)\n"
    "4. Experience (timeline or cards)\n"
    "5. Projects (gallery or grid with hover)\n"
    "6. Education\n"
    "7. Contact (with working form and validation JS)\n\n"
    
    "Output everything as a **self-contained .html** file with all styles in `<style>` and all scripts in `<script>`. "
    "Make sure the visual design is eye-catching, stylish, and colorful.\n\n"
    
    f"Resume:\n{resume_text}"
)




        response = model.generate_content(prompt)

        return response.text if hasattr(response, "text") else str(response)

    except Exception as e:
        return f"❌ Error generating site: {e}"

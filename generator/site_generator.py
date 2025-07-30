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
        # ✅ Use Gemini 2.5 Flash model
        model = genai.GenerativeModel("gemini-2.5-flash")

        prompt = (
    "🎨 You are an EXPERT front-end designer who creates STUNNING, HIGHLY ANIMATED portfolio websites. "
    "Generate a **SPECTACULAR single-page portfolio** using HTML, CSS, and JavaScript in ONE file.\n\n"
    
    "🚀 ANIMATION REQUIREMENTS (MANDATORY):\n"
    "- **Particle background** with floating geometric shapes or stars\n"
    "- **Typewriter effect** for name and main headings\n"
    "- **Fade-in animations** for every section (staggered timing)\n"
    "- **Slide-in effects** from left/right for content blocks\n"
    "- **Bounce/pulse animations** for skill bars and progress indicators\n"
    "- **Hover animations** with scale, glow, and color transitions\n"
    "- **Floating/bobbing icons** and emoji elements\n"
    "- **Smooth parallax scrolling** effects\n"
    "- **Interactive cursor trail** or custom cursor\n"
    "- **Loading screen** with animated logo/name\n"
    "- **Morphing gradient backgrounds** that change colors\n"
    "- **Rotate/flip animations** on cards and buttons\n\n"
    
    "🎯 VISUAL DESIGN (SPECTACULAR):\n"
    "- **Neon gradients** and **glassmorphism** effects\n"
    "- **Vibrant color palette**: Electric blues, neon purples, gold accents\n"
    "- **Multiple background layers** with gradients and patterns\n"
    "- **Box shadows** with multiple layers and glow effects\n"
    "- **Border radius** and **backdrop filters** for modern look\n"
    "- **Google Fonts**: Use 2-3 complementary modern fonts\n"
    "- **CSS transforms** for 3D effects and perspective\n\n"
    
    "😍 EMOJI INTEGRATION (EVERYWHERE):\n"
    "- Add relevant emojis to ALL section headings\n"
    "- Use emojis as bullet points and decorative elements\n"
    "- Animated emoji reactions on hover\n"
    "- Emoji progress indicators for skills\n"
    "- Floating emoji particles in the background\n"
    "- Emoji-based navigation indicators\n\n"
    
    "📱 RESPONSIVE & INTERACTIVE:\n"
    "- **Mobile-first** design with perfect responsive behavior\n"
    "- **Touch-friendly** animations and interactions\n"
    "- **Intersection Observer** for scroll-triggered animations\n"
    "- **Smooth scrolling** navigation with active states\n\n"

    "🔧 ADVANCED FEATURES:\n"
    "- **Dynamic theme switcher** (light/dark mode toggle)\n"
    "- **Skill bars** with animated percentage fills\n"
    "- **Project cards** with flip animations and hover previews\n"
    "- **Timeline animations** for experience section\n"
    "- **Contact form** with real-time validation and animations\n"
    "- **Social media icons** with bounce/glow effects\n\n"

    "📂 REQUIRED SECTIONS:\n"
    "1. 🚀 **Loading Screen** (animated logo/name reveal)\n"
    "2. 🌟 **Hero Section** (full-screen with particle background)\n"
    "3. 👨‍💻 **About Me** (with typewriter bio and floating elements)\n"
    "4. 💪 **Skills** (animated progress bars with emoji indicators)\n"
    "5. 💼 **Experience** (interactive timeline with hover details)\n"
    "6. 🎯 **Projects** (card grid with flip animations)\n"
    "7. 🎓 **Education** (timeline or certificate cards)\n"
    "8. 📞 **Contact** (animated form with emoji feedback)\n"
    "9. 🔗 **Footer** (social links with hover animations)\n\n"
    
    "💻 TECHNICAL REQUIREMENTS:\n"
    "- All code in ONE HTML file (embedded CSS and JS)\n"
    "- Use modern CSS features: grid, flexbox, custom properties\n"
    "- Implement smooth 60fps animations with CSS transforms\n"
    "- Add loading states and performance optimizations\n"
    "- Include meta tags for SEO and social sharing\n\n"
    
    "🎨 ANIMATION TIMING:\n"
    "- Loading screen: 2-3 seconds\n"
    "- Section reveals: 0.6s delay between elements\n"
    "- Hover effects: 0.3s smooth transitions\n"
    "- Scroll animations: triggered at 20% viewport\n\n"
    
    "Make this portfolio absolutely STUNNING and UNFORGETTABLE! 🔥✨🌈\n\n"
    
    f"Resume Content:\n{resume_text}"
)

        response = model.generate_content(prompt)
        return response.text if hasattr(response, "text") else str(response)

    except Exception as e:
        return f"❌ Error generating site: {e}"

def save_portfolio_site(html_content: str, filename: str = "portfolio.html"):
    """Save the generated HTML content to a file"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"✅ Portfolio saved as {filename}")
        return True
    except Exception as e:
        print(f"❌ Error saving file: {e}")
        return False

# Example usage function
def create_portfolio_from_resume(resume_file_path: str = None, resume_text: str = None):
    """
    Create a portfolio from either a resume file or direct text input
    """
    if resume_file_path:
        try:
            with open(resume_file_path, 'r', encoding='utf-8') as f:
                resume_content = f.read()
        except Exception as e:
            print(f"❌ Error reading resume file: {e}")
            return None
    elif resume_text:
        resume_content = resume_text
    else:
        print("❌ Please provide either resume_file_path or resume_text")
        return None
    
    print("🚀 Generating your spectacular animated portfolio...")
    html_content = generate_portfolio_site(resume_content)
    
    if html_content and not html_content.startswith("❌"):
        save_portfolio_site(html_content)
        print("🎉 Your amazing portfolio is ready! Open portfolio.html in your browser.")
        return html_content
    else:
        print("❌ Failed to generate portfolio")
        return None

# Example usage:
if __name__ == "__main__":
    # Option 1: From resume file
    # create_portfolio_from_resume("resume.txt")
    
    # Option 2: From direct text
    sample_resume = """
    John Doe
    Full Stack Developer
    
    SKILLS:
    - JavaScript, React, Node.js
    - Python, Django, Flask
    - HTML5, CSS3, Bootstrap
    - MongoDB, PostgreSQL
    - Git, Docker, AWS
    
    EXPERIENCE:
    Senior Developer at TechCorp (2022-Present)
    - Built scalable web applications
    - Led team of 5 developers
    
    EDUCATION:
    Computer Science Degree, MIT (2020)
    """
    
    create_portfolio_from_resume(resume_text=sample_resume)
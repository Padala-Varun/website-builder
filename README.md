# 🛠️ Resume to Portfolio Website Builder

Transform your resume into a stunning, colorful, and modern **portfolio website** using Google Gemini AI ✨. This tool lets users upload a PDF resume and automatically generates a **fully responsive**, **single-page personal portfolio site** — complete with smooth scroll, vibrant gradients, animated sections, and more.

---

## 🚀 Features

<<<<<<< HEAD
- 🔄 **One-Click Resume to Website Conversion**
- 📄 Upload your **PDF resume**, and AI generates a portfolio site
- 🎨 **Modern design** with:
  - Vibrant color **gradients**
  - Stylish fonts via **Google Fonts**
  - **Glassmorphism**, shadows, and hover effects
- 📱 **Responsive Layout** using Flexbox and Media Queries
- 💡 Interactive JS features:
  - Smooth scrolling
  - Sticky navigation bar
  - Scroll-triggered animations
  - Contact form with validation
- 📂 Structured Website Sections:
  1. Hero Section
  2. About Me
  3. Skills (with progress bars)
  4. Experience
  5. Projects
=======
- **app.py**: The main entry point for the Streamlit application, handling the frontend interface and user interactions.
- **extractor/**: A module for extracting and structuring data from resumes.
  - **__init__.py**: Initializes the extractor module.
  - **pdf_loader.py**: Contains functions to extract text from PDF files.
  - **resume_parser.py**: Structures the content of resumes.
- **generator/**: A module for generating HTML content.
  - **__init__.py**: Initializes the generator module.
  - **site_generator.py**: Generates HTML content based on prompts from the Gemini API.
- **templates/**: Contains optional HTML templates for rendering.
  - **base_template.html**: Base template for the frontend.
- **output/**: Directory for generated output files.
  - **site.html**: The final HTML representation of the user's portfolio.
- **.env**: Stores environment variables, including the Gemini API key.
- **requirements.txt**: Lists the Python dependencies required for the project.
- **README.md**: Documentation for the project.

## Setup Instructions

1. Clone the repository:
   ```
   git clone 
   cd website-builder
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up your environment variables in the `.env` file, including your Gemini API key.

## Usage

To run the application, execute the following command:
```
streamlit run app.py
```

Follow the instructions in the Streamlit interface to upload your resume and generate your portfolio website.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
>>>>>>> a89972431a90b28ab10489179d6114fcf4305505

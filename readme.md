**AI Job Match Analyzer**
==============================

A powerful NLP + LLM-powered tool that analyzes a Job Description and a Resume, compares skills, computes match percentage, highlights missing skills, and generates AI-optimized resume improvement suggestions.

Built with **Python, spaCy, RapidFuzz, Groq LPU inference, and Streamlit**.

🚀 **Features**
---------------

*   Extracts skills & keywords from both JD and Resume
    
*   Computes:
    
    *   **Match Percentage**
        
    *   **Missing Skills**
        
    *   **Matched Skills**
        
    *   **Resume Score**
        
*   Generates:
    
    *   **Smart resume improvement bullets**
        
    *   **A professional headline**
        
    *   **A rational explanation of the match**
        
*   Clean, modern **UI with colored sections and skill badges**
    
*   Fully local processing except LLM suggestions
    

🧰 **Tech Stack**
-----------------

*   **Python 3.10+**
    
*   **spaCy** for NLP
    
*   **RapidFuzz** for fuzzy skill matching
    
*   **Groq API (Llama 3.1 70B)** for AI suggestions
    
*   **Streamlit** for the UI
    
*   **HTML + inline CSS** for styling
    

📂 **Project Structure**
------------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   ai_job_analyzer/  │── analyzer.py          # Core logic: NLP, matching, scoring, LLM suggestions  │── model_interface.py   # Groq model wrapper  │── app.py               # Streamlit UI  │── requirements.txt  │── demo_output_examples/  │     └── example_output.json  │── README.md   `

🖥️ **How It Works**
--------------------

### 1️⃣ Extract Candidate Skills

Using spaCy noun-chunks + entities + token filtering.

### 2️⃣ Compute Match %

Compares JD vs Resume skill tokens using RapidFuzz.

### 3️⃣ Generate AI Suggestions

Uses Groq Llama 3.1 70B to create:

*   3 resume bullets
    
*   1 headline
    
*   1 rationale
    

### 4️⃣ Present Output in Beautiful UI

Sections:

*   Skills extracted
    
*   Missing skills as badges
    
*   Match & resume scores
    
*   AI resume suggestions
    

▶️ **Run Locally**
------------------

### **Install packages**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pip install -r requirements.txt   `

### **Run Streamlit app**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   streamlit run app.py   `

🔑 **Setup Groq API Key**
-------------------------

Create .env file:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   GROQ_API_KEY=your_api_key_here   `

📝 **Example Inputs**
---------------------

### Job Description (JD)

(Include the sample JD text you used in the demo)

### Resume

(Include the sample resume text you used)

📸 **Demo Screenshot (Optional)**
---------------------------------

Add a screenshot of your tool here.

⭐ **Future Improvements**
-------------------------

*   Skill ontology mapping
    
*   Support for PDF/Docx uploads
    
*   ATS score
    
*   Resume rewriting
    
*   Multi-language support
    

🤝 **Contributing**
-------------------

Pull requests are welcome!

📬 **Contact**
--------------

If you want this as a SaaS product or need customization, feel free to contact me.
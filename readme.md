**AI Job Match Analyzer**
==============================
<p align="center">
  <img src="https://img.shields.io/badge/LLM-Llama3.1_70B-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Groq-LPU_Inference-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Python-3.10+-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge" />
</p>

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
```
 ai_job_analyzer/
│── analyzer.py          
│── model_interface.py   
│── app.py               
│── requirements.txt
│── examples/
│     └── job_desc.txt
|     └── resume.txt
│── README.md
```

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

```   
pip install -r requirements.txt
pip install streamlit groq
python -m spacy download en_core_web_sm
```

### **Run Streamlit app**

```
streamlit run app.py
```

🔑 **Setup Groq API Key**
-------------------------

Login to your groq dashborad and then create new API key. Copy that key and then set it as an environment variable using:

```
export GROQ_API_KEY="your_api_key_here" (FOR Linux/Mac)
```
```
setx GROQ_API_KEY "your_api_key_here" (FOR Powershell)
```

After that kill your terminal and reopen to ensure changes, also run the below to check:
```
echo $env:GROQ_API_KEY
```


📝 **Example Inputs**
---------------------

### Job Description (JD)
```
We are seeking a Senior Data Engineer with 5+ years of experience in Python development and data engineering. 
The candidate should have experience with cloud-based solutions, building scalable data pipelines, 
working with cross-functional teams, ETL workflows, and ensuring data quality, integrity, and performance. 
Strong knowledge of distributed systems, automated testing, CI/CD pipelines, and production deployments 
on cloud platforms (AWS, GCP, or Azure) is required. Familiarity with data applications, documentation 
of technical specifications and best practices, relational databases, NoSQL databases (MongoDB), 
REST APIs, microservices, message queues (Kafka), cloud infrastructure, DevOps tools, Kubernetes, Terraform, 
and other CI/CD tools is strongly preferred.
```

### Resume
```
I am a software engineer with 3 years of experience in Python and SQL. 
I have built ETL pipelines, used Docker and Kubernetes for containerized deployment, 
and deployed small-scale data applications on AWS. I am familiar with relational databases, 
basic CI/CD pipelines, and some cloud infrastructure tools. I have collaborated with small teams 
on several projects, focusing on data processing and analysis.
```

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

📹 **Demo Video**
-------------------

Youtube:

📬 **Contact**
--------------

If you want this as a SaaS product or need customization, feel free to contact me.

📄 **License**
--------------

MIT

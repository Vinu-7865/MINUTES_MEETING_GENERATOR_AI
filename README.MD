# 🚀 MinuteMaster AI - Executive Meeting Minutes Generator

**Status:** Capstone Project Requirement  
**Role:** Architect & Lead Software Engineer  
**Core Stack:** Python 3.10+, Streamlit, Gemini 2.5 Flash, Pydantic Structural Contracts, Python-Dotenv

---

## 📋 1. Application Purpose & Functionality

In modern corporate environments, unstructured business meetings generate chaotic, non-linear dialogues. Critical deadlines, task assignments, and core strategic decisions are easily lost within conversational noise and off-topic banter.

**MinuteMaster AI** addresses this systemic operational inefficiency. It acts as an automated data distillation framework that ingests raw, messy, conversational meeting transcripts and processes them into structured, executive-ready operational intelligence. 

### Key Capabilities:
- **Intelligent Dialogue Distillation:** Leverages the semantic reasoning of Gemini 2.5 Flash to map text into structured parameters.
- **Noise Elimination Architecture:** Automatically filters out conversational filler and off-topic discussion tracks (e.g., casual water-cooler chatter) to keep records strictly business-focused.
- **Deterministic Component Rendering:** Formats extracted entities into distinct UI sections including an Executive Summary, Participant Badges, Key Discussion Strands, and Core Decisions.
- **Action Item Automation:** Programmatically isolates deliverables, links them directly to their specific human owners, and extracts target completion timelines.

---

## 🛠️ 2. Key Technologies & Libraries Used

To maintain a clean, enterprise-grade architecture, the platform decouples the ingestion layer from the user interface using the following framework stack:

1. **Python 3.10+**: The foundational baseline language optimized for script execution and object-oriented data schemas.
2. **Streamlit**: Utilized as a reactive UI layer to create an administrative workspace dashboard without frontend overhead.
3. **google-genai**: The official Google SDK engineered to securely establish low-latency pipelines with the Gemini 2.5 Flash model.
4. **Pydantic**: Enforces strict typing and data validation contracts on incoming model parameters, ensuring unstructured data fits rigid UI requirements.
5. **Python-Dotenv**: Manages local execution configurations by abstracting and securing system environment variables (API credentials).

---

## ⚙️ 3. Installation Instructions

1. **Create the virtual environment**

   ```bash
   python -m venv venv
   ```

2. **Activate it**

   * Git Bash:

     ```bash
     source venv/Scripts/activate
     ```
   * Windows Command Prompt:

     ```cmd
     venv\Scripts\activate.bat
     ```
   * Windows PowerShell:

     ```powershell
     .\venv\Scripts\Activate.ps1
     ```

3. **Install dependencies**

   ```bash
   python -m pip install streamlit google-genai pydantic python-dotenv
   ```

4. **Create a `.env` file**

   ```text
   GEMINI_API_KEY=YOUR_API_KEY_HERE
   ```

   Keep the key private and avoid committing the `.env` file to version control. A common `.gitignore` entry is:

   ```text
   .env
   venv/
   ```

5. **Run the application**

   ```bash
   python -m streamlit run main.py
   ```

If everything is configured correctly, Streamlit will start a local web server and display a URL such as:

```text
Local URL: http://localhost:8501
```

Open that URL in your browser to use the app.

If you're encountering an error while following these steps, paste the error message and I can help diagnose it.

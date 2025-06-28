# 🛍️ AI Shopping Agent

An AI-powered shopping assistant that suggests personalized product recommendations based on your preferences and budget. Built using Streamlit, Cohere LLMs, and SerpAPI.

![App Screenshot](assets/background.png)

---

## 🚀 Features

- 🧠 AI-powered product suggestions using Cohere's LLMs  
- 🔍 Real-time product search using SerpAPI  
- 🎯 Budget-aware and preference-based filtering  
- 🖼️ Clean e-commerce themed UI with a custom background  
- 🔒 Secrets like API keys stored securely via `.streamlit/secrets.toml`

---

## 🧰 Tech Stack

| Component      | Technology            |
|----------------|------------------------|
| Backend LLM    | [Cohere AI](https://cohere.com/) |
| Product Search | [SerpAPI](https://serpapi.com/) |
| UI Framework   | [Streamlit](https://streamlit.io/) |
| Language       | Python 3.10+           |
| Deployment     | Local / Streamlit Cloud |

---

## 📂 Project Structure

shopping-agent/
├── app.py
├── requirements.txt
├── .gitignore
├── assets/
│ └── background.png
├── .streamlit/
│ └── secrets.toml # Do not commit this
└── README.md


---

## 🔑 Setup & Installation

### 1. Clone the Repo
```bash
git clone https://github.com/kamanaHarikrishna/shopping-agent.git
cd shopping-agent


2. Set Up Virtual Environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate        # Windows
# or
source venv/bin/activate     # Mac/Linux

3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt

4. Create .streamlit/secrets.toml
toml
Copy
Edit
COHERE_API_KEY = "your-cohere-key"
SERPAPI_KEY = "your-serpapi-key"

💻 Run the App Locally
bash
Copy
Edit
streamlit run app.py

🙋‍♂️ Developed By
Hari Krishna Kamana
LinkedIn • GitHub

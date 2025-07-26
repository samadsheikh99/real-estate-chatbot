# 🏘️ AI-Powered Real Estate Listing Generator

This project is an AI-based application that automatically generates attractive and realistic real estate listing descriptions using Large Language Models (LLMs) via Hugging Face. It supports both backend (FastAPI) and frontend (Streamlit) interfaces.

---

## 🚀 Project Structure
Real-Estate_chatbot/
│
├── backend/ # FastAPI backend with LLM integration
│ ├── main.py # API routes and LangChain logic
│ ├── utils.py # Helper functions
│ └── requirements.txt # Backend dependencies
│
├── frontend/ # Streamlit web interface
│ └── app.py # Frontend logic that communicates with the backend
│
├── .env # Environment variables (API keys)
├── .gitignore # Files and folders to ignore in Git

---

## 🧠 How It Works

1. **User Input**: User enters property details like type, location, area, etc.  
2. **FastAPI Backend**: Sends data to Hugging Face model via LangChain.  
3. **LLM**: Model like `Mixtral-8x7B-Instruct` or `Flan-T5` generates listing description.  
4. **Frontend**: Streamlit app displays the generated result.

---

## 🛠️ Technologies Used

- **LangChain** (`langchain`, `langchain-huggingface`)
- **Hugging Face Hub** (for LLMs like `Mixtral-8x7B-Instruct`, `Flan-T5`)
- **FastAPI** (backend API for LLM interaction)
- **Streamlit** (frontend UI)
- **Python 3.13**
- **Docker** (for containerization)

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/real-estate-chatbot.git
cd real-estate-chatbot

python -m venv real_estate
real_estate\Scripts\activate  # For Windows

 Install Requirements
pip install -r requirements.txt

Set Environment Variables
Create a .env file in the root:
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token

▶️ Running the Project
Start FastAPI Backend
cd backend
uvicorn main:app --reload
API runs on http://localhost:8000

Start Streamlit Frontend
In a new terminal:
cd frontend
streamlit run app.py

App opens in your browser: http://localhost:8501


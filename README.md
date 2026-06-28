# Cold Email Generator

AI-powered cold email generator that scrapes job postings, extracts key requirements using LLMs, and writes personalized cold emails with relevant portfolio links — all through a Streamlit web interface.

## Overview

This project automates the cold email writing process for business development. Given a job posting URL, the system:
1. Scrapes the job posting content
2. Uses an LLM to extract role, skills, experience, and description
3. Matches extracted skills against a portfolio database using vector search
4. Generates a personalized cold email referencing relevant past work

## How It Works

```
Job URL → Web Scraping → LLM Extraction → Skill Matching (Vector DB) → Email Generation
```

- **Web Scraping**: Uses LangChain's WebBaseLoader to fetch and parse job posting pages
- **LLM Extraction**: Groq-hosted Llama 3 (70B) extracts structured job info (role, skills, experience)
- **Vector Search**: ChromaDB stores portfolio entries as embeddings; matches job skills to relevant portfolio links
- **Email Generation**: LLM writes a tailored cold email incorporating job requirements and matched portfolio items

## Tech Stack

- **Python** — Core language
- **LangChain** — LLM orchestration, prompt templates, chains
- **Groq API** — Llama 3 70B inference
- **ChromaDB** — Vector store for portfolio matching
- **Streamlit** — Web interface
- **Pandas** — Portfolio data management

## Project Structure

```
ColdEmailGenerator/
├── main.py              # Streamlit app entry point
├── chains.py            # LLM chains for extraction & email writing
├── portfolio.py         # ChromaDB vector store for portfolio matching
├── text_preprocessor.py # Web content cleaning utilities
├── requirements.txt     # Python dependencies
├── assets/              # Portfolio data (CSV with tech stack & links)
└── vector_store/        # ChromaDB persistent storage
```

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Pramod-Pasala/ColdEmailGenerator.git
   cd ColdEmailGenerator
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Prepare portfolio data**:
   Add your portfolio entries to `assets/portfolio.csv` with columns: `Techstack`, `Links`

5. **Run the app**:
   ```bash
   streamlit run main.py
   ```

## Usage

1. Open the app in your browser
2. Paste a job posting URL
3. Click "Generate Cold Email"
4. The system scrapes the page, extracts job info, matches your portfolio, and generates a personalized email

## License

This project is open source — feel free to use and modify.

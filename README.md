# Smart Prompting Toolkit

A modular toolkit to automate, evaluate, and optimize prompt engineering workflows using GPT-based LLMs. This toolkit enables configurable prompt chaining, dynamic variable injection, and scoring across NLP tasks such as summarization, classification, and Q&A.

Built to support researchers and ML teams experimenting with different prompt designs, chaining logic, and hallucination evaluation — all from a single interface.

---

## Features

- Run and chain multiple prompt templates
- Inject variables dynamically into base templates
- Evaluate LLM outputs for accuracy, coherence, and hallucinations
- Generate performance reports across tasks (e.g., summarization, classification)
- Visualize token usage, response confidence, and hallucination rate

---

## Tech Stack

- Python
- OpenAI API / Hugging Face Transformers
- Streamlit (for UI)
- LangChain (prompt chaining and execution)
- matplotlib / seaborn (for metrics)
- pandas

---

## Project Structure

    smart-prompting-toolkit/
    │
    ├── app/ # Streamlit app or CLI scripts
    ├── prompts/ # Template prompt JSON or TXT files
    ├── results/ # Model outputs and evaluation logs
    ├── utils/ # Scoring, hallucination checks, etc.
    ├── README.md
    ├── requirements.txt
    └── .gitignore


---

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/smart-prompting-toolkit.git
    cd smart-prompting-toolkit
    python -m venv venv
    source venv/bin/activate   # Windows: venv\Scripts\activate
    pip install -r requirements.txt
    streamlit run app/main.py 

## Future Improvements

- Support for local LLMs via Ollama or Transformers
- Export to PDF/CSV with full output + metrics
- Chain-of-thought prompt templates
- Integration with LangChain agents



## License

This project is licensed under the MIT License.









# AI Research Paper Implementation Agent

This project is a LangGraph-based AI system that transforms machine learning research papers into executable PyTorch implementations with explanations and GitHub-based retrieval support.

The goal of this project is to help users understand research papers not only through summaries, but through generated implementations that are mapped back to the concepts and sections of the paper itself.


---

# Features

* Upload ML research papers in PDF format
* Extract and analyze paper methodology
* Generate implementation plans using LLMs
* Search GitHub for related implementations
* Generate PyTorch code implementations
* Generate beginner-friendly paper summaries
* Generate explanations mapping code back to paper concepts
* Multi-node LangGraph orchestration workflow
* FastAPI backend + Streamlit frontend
* Dockerized multi-container architecture
* Cloud deployment support (Render + Streamlit Cloud)

---

# Project Architecture

```text
User
  │
  ▼
Streamlit Frontend
  │
  ▼
FastAPI Backend
  │
  ▼
LangGraph Workflow
  │
  ├── Planner Node
  ├── GitHub Search Node
  ├── Coder Node
  ├── Summary Node
  ├── Explanation Node
  └── Packager Node
  │
  ▼
Generated Outputs
```

---

# LangGraph Workflow

```text
START
 ↓
Planner Node
 ↓
GitHub Search Node
 ↓
Coder Node
 ↓
Summary Node
 ↓
Explanation Node
 ↓
Packager Node
 ↓
END
```

---

# Shared State Design

The system uses a shared LangGraph state object passed between nodes during execution.

```python
class PaperState(TypedDict):

    pdf_text: str

    paper_title: str

    extracted_title: str

    plan: str

    github_repos: List[dict]

    generated_code: str

    paper_summary: str

    explanation: str

    output_package: dict

    current_step: str
```

Each node:

* reads relevant state fields
* updates specific fields
* passes enriched state forward

This creates a stateful orchestration workflow instead of a single prompt chain.

---

# Node Responsibilities

## Planner Node

* Reads extracted PDF text
* Uses Groq LLM to analyze paper
* Extracts title, methodology, architecture, and implementation plan

## GitHub Search Node

* Uses extracted paper title
* Searches GitHub for related implementations
* Retrieves repositories and metadata

## Coder Node

* Uses implementation plan + retrieved repositories
* Generates PyTorch implementation code

## Summary Node

* Generates beginner-friendly explanation of paper

## Explanation Node

* Maps generated code back to paper concepts

## Packager Node

* Creates final output artifacts
* Saves generated files

---

# Tech Stack

## AI / Orchestration

* LangGraph
* Groq API
* Llama 3.3 70B

## Backend

* FastAPI

## Frontend

* Streamlit

## Retrieval

* PyGithub

## PDF Processing

* pypdf

## Deployment

* Docker
* Render
* Streamlit Cloud

---

# Project Structure

```text
ResearchPaper_implementationAgent/
│
├── backend/
│   ├── graph/
│   │   ├── nodes/
│   │   ├── graph.py
│   │   └── state.py
│   │
│   ├── prompts/
│   ├── tools/
│   ├── main.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── app.py
│   ├── styles.css
│   ├── Dockerfile
│   └── requirements.txt
│
├── outputs/
├── docker-compose.yml
├── .env
└── README.md
```

---

# Generated Outputs

The system generates:

```text
implementation.py
paper_summary.md
explanation.md
references.md
```

---

# Deployment Architecture

```text
User Browser
      │
      ▼
Streamlit Cloud
(Frontend)
      │
 HTTPS Requests
      │
      ▼
Render Backend
(FastAPI + LangGraph)
      │
      ├── Groq API
      └── GitHub API
```

---

# Dockerized Architecture

Frontend and backend are containerized separately.

```text
Docker Compose
│
├── Frontend Container
│     └── Streamlit
│
└── Backend Container
      └── FastAPI + LangGraph
```

This allows:

* isolated environments
* reproducible deployments
* independent services
* easier scaling

---

# Local Setup

## Clone Repository

```bash
git clone https://github.com/abd-04/ResearchPaper_implementationAgent
cd ResearchPaper_implementationAgent
```

---

## Create Environment Variables

Create `.env`

```env
GROQ_API_KEY=your_key
GITHUB_TOKEN=your_token
```
---

## Manual Local Setup (Without Docker)

```bash
# Create virtual environment
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```
---

## Install Backend Dependencies

```bash
pip install -r backend/requirements.txt
```

---

## Install Frontend Dependencies

```bash
pip install -r frontend/requirements.txt
```

---

## Run Backend

```bash
uvicorn backend.main:app --reload
```

Backend runs on:

```text
http://localhost:8000
```

---

## Run Frontend

```bash
streamlit run frontend/app.py
```

Frontend runs on:

```text
http://localhost:8501
```

---

## Run With Docker

```bash
docker-compose up --build
```

Frontend:

```text
http://localhost:8501
```

Backend:

```text
http://localhost:8000/docs
```

---

# Cloud Deployment

## Backend

* Render
* Docker deployment

## Frontend

* Streamlit Community Cloud

Environment variables are configured using platform secrets.

---

# Key Learning Outcomes

This project helped explore:

* AI orchestration systems
* LangGraph stateful workflows
* Retrieval-Augmented Generation (RAG)
* Backend engineering
* FastAPI APIs
* Docker containerization
* Multi-service architecture
* Cloud deployment
* Environment variable management
* LLM application design

---



---

# Features to include later:

Planned future features:

* Vision/diagram parsing
* Tavily web search
* Multi-agent reasoning expansion
* Live workflow visualization
* ZIP export packages
* Better implementation validation
* Multi-paper support

---



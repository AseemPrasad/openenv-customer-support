

# OpenEnv Customer Support Chat Assistant

## Overview
This repository contains an **OpenEnv environment** that simulates a real-world **customer support chat assistant**.  
The goal is to provide a benchmark environment for training and evaluating AI agents on realistic customer support tasks.

Agents interact with simulated customers through text-based conversations, aiming to resolve queries, maintain satisfaction, and escalate appropriately when needed.

---

## Features
- **Spec compliant**: Implements `step()`, `reset()`, `state()` with typed Pydantic models.
- **Three tasks with deterministic graders**:
  - Easy: Single FAQ query.
  - Medium: Sequential queries with sentiment variation.
  - Hard: Multiple simultaneous customers with conflicting needs.
- **Reward function**: Centralized in `rewards.py` for modularity and testing.
- **Baseline inference script**: `inference.py` demonstrates reproducible scoring (OpenAI API or mock agent).
- **Deployment ready**: Dockerfile + Hugging Face Spaces integration.
- **Validated**: Passes `openenv validate` for multi‑mode deployment.

---

## Repository Structure
```
openenv-customer-support/
│
├── README.md              # Project documentation
├── openenv.yaml           # Environment metadata
├── pyproject.toml         # Project configuration
├── uv.lock                # Dependency lock file
├── inference.py           # Baseline inference script
├── Dockerfile             # Containerization for Hugging Face Spaces
├── server/
│   └── app.py             # FastAPI entry point for OpenEnv server
├── src/
│   └── chat_env/          # Environment implementation
│       ├── __init__.py
│       ├── models.py      # Pydantic models for state/action/reward
│       ├── env.py         # Environment class with step/reset/state
│       ├── tasks.py       # Task definitions and graders
│       ├── rewards.py     # Reward shaping logic
│       └── server.py      # Alternate server entry point
└── tests/
    ├── test_env.py        # Unit tests for environment
    └── test_rewards.py    # for reward validation
```

---

## Quick Start

### Installation
Clone the repository:
```bash
git clone https://github.com/<your-username>/openenv-customer-support.git
cd openenv-customer-support
```

Install dependencies:
```bash
pip install uv
uv sync
```

### Running Locally
```bash
uv run server --host 0.0.0.0 --port 8000
```

### Validation
```bash
openenv validate
```

### Inference
Run baseline inference (requires OpenAI API key):
```bash
setx OPENAI_API_KEY "your_api_key_here"   # Windows PowerShell
python inference.py
```

Or switch to a mock agent by editing `inference.py` to avoid API usage.

---

## Deployment
This environment is designed to be deployed as a Hugging Face Space with the `openenv` tag.  
Deployment steps:
1. Push repo to GitHub.
2. Create a new Hugging Face Space (Docker mode).
3. Link to your GitHub repo.
4. Space will build automatically using the provided Dockerfile.

---

## License
MIT License

---


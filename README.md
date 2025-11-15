# Smart Concierge — Autonomous Multi-Agent Travel Planner

This repository contains a multi-agent travel planning system (Coordinator, Search Agent, Validation Agent, Booking Agent) designed for the Capstone project. The system is intentionally modular and uses FastAPI for each agent so they can run as independent services.

## What’s included
- Coordinator (LLM-driven orchestrator, mocked LLM client)
- Search Agent (mock search APIs)
- Validation Agent (budget, timing checks)
- Booking Agent (OpenAPI-like booking simulator with pause/resume)
- Memory store (simple SQLite/JSON store)
- Tools (price compare, calendar sync)
- Tests and a demo notebook

## Quickstart (local, mocked)
Requirements: Python 3.10+, Docker (optional)

### 1. Create virtualenv and install

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

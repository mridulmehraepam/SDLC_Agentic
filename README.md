# SDLC_Agentic

Push Hogya

## Agent Definitions

| Agent | File | Role |
|---|---|---|
| Product Manager | [agents/product-manager-agent.md](agents/product-manager-agent.md) | Requirements & scope |
| Project Scaffolding | [agents/project-scaffolding-agent.agent.md](agents/project-scaffolding-agent.agent.md) | Build project structure from requirements.md |
| Backend Architecture | [agents/backend-architecture.md](agents/backend-architecture.md) | Scalable backend design |
| Backend API Design | [agents/backend-api-design.agent.md](agents/backend-api-design.agent.md) | REST API spec from data models |
| AI Integration | [agents/ai-integration-agent.agent.md](agents/ai-integration-agent.agent.md) | EPAM AI DIAL endpoint design |
| Workflow Diagram | [agents/workflow-diagram-agent.agent.md](agents/workflow-diagram-agent.agent.md) | Mermaid sequence diagrams |

## Shared Project Context

All agents read and update [project-context.md](project-context.md) to stay in sync.

## Run Locally

### Backend (FastAPI)

```powershell
cd c:/autocode/agenticAISession/SDLC_Agentic
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000
```

Backend URLs:

- API root health: `http://127.0.0.1:8000/health`
- Swagger docs: `http://127.0.0.1:8000/docs`

### Frontend (React + Vite)

Prerequisite: Install Node.js (which includes npm), then run:

```powershell
cd c:/autocode/agenticAISession/SDLC_Agentic
npm install
npm run dev
```

Frontend URL:

- App: `http://127.0.0.1:5173`
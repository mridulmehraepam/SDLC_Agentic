# 🎙️ Podcast Episode Planner - SDLC Agentic Demo

A multi-agent system demonstrating the **Blackboard Pattern** for building software using AI agents.

## 🌟 Overview

This project showcases a **5-agent pipeline** that collaboratively builds a complete Podcast Episode Planner application:

```
You → Spectra → Nexus → Oracle → Canvas → Scribe → Complete Design Doc
         ↓         ↓        ↓        ↓         ↓
      [=================== shared/project_context.md ===================]
```

**No agent communicates directly with another** — they all read/write to a shared markdown file (Blackboard Pattern).

## 🤖 Agent Roster

| # | Agent | Avatar | Role |
|---|-------|--------|------|
| 1 | **Spectra** | 📋 | Requirements Architect - Data models & specifications |
| 2 | **Nexus** | 🔌 | API Architect - REST endpoints & contracts |
| 3 | **Oracle** | 🤖 | AI Specialist - EPAM AI DIAL integration |
| 4 | **Canvas** | 🎨 | UI Architect - React components & user flows |
| 5 | **Scribe** | 📊 | Documentation Master - Diagrams & summaries |

## 📁 Project Structure

```
podcast-planner/
├── .github/
│   ├── agents/              ← Agent definitions (JSON)
│   │   ├── spectra.json
│   │   ├── nexus.json
│   │   ├── oracle.json
│   │   ├── canvas.json
│   │   └── scribe.json
│   └── copilot-instructions.md
├── agents/                  ← Agent prompts (Markdown)
│   ├── agent1_requirements.md
│   ├── agent2_api.md
│   ├── agent3_ai.md
│   ├── agent4_ui.md
│   └── agent5_docs.md
├── shared/
│   └── project_context.md   ← THE BLACKBOARD (shared output)
└── frontend/
    ├── home.html            ← Landing page
    ├── index.html           ← Agent Pipeline UI
    └── app.html             ← Working Podcast Planner App
```

## 🚀 Quick Start

### Option 1: Open the Demo UI
1. Open `podcast-planner/frontend/home.html` in your browser
2. Choose either **Agent Pipeline** or **Podcast Planner App**

### Option 2: Run the Agent Pipeline
1. Open VS Code with this workspace
2. Press `Ctrl + Shift + I` to open Copilot Chat
3. Set mode to **"Agent"** (not "Ask")
4. Run each agent in sequence:

```
@spectra Read agents/agent1_requirements.md and execute
@nexus Read agents/agent2_api.md and execute  
@oracle Read agents/agent3_ai.md and execute
@canvas Read agents/agent4_ui.md and execute
@scribe Read agents/agent5_docs.md and execute
```

5. Check `shared/project_context.md` for complete output

## 🎯 Features Built by the Pipeline

### Episode Management
- Create, View, Edit, Delete episodes
- Fields: Title, Topic, Episode Number, Planned Date
- Status workflow: Draft → Scripted → Published

### Guest Management  
- Add guests with Name, Bio, Area of Expertise
- Link guests to episodes
- Full CRUD operations

### AI Integration (EPAM AI DIAL)
- **Script Generator**: Topic + Guest Bio → Full interview script
- **Question Bank**: Topic + Expertise → 10 interview questions

## 🔧 How the Blackboard Pattern Works

```
┌─────────┐     ┌─────────┐     ┌─────────┐     ┌─────────┐     ┌─────────┐
│ Spectra │     │  Nexus  │     │ Oracle  │     │ Canvas  │     │ Scribe  │
│  (Req)  │     │  (API)  │     │  (AI)   │     │  (UI)   │     │ (Docs)  │
└────┬────┘     └────┬────┘     └────┬────┘     └────┬────┘     └────┬────┘
     │               │               │               │               │
     ▼               ▼               ▼               ▼               ▼
┌────────────────────────────────────────────────────────────────────────┐
│                     shared/project_context.md                          │
│                         (THE BLACKBOARD)                               │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐          │
│  │Section 1│ │Section 2│ │Section 3│ │Section 4│ │Section 5│          │
│  │  Data   │ │   API   │ │   AI    │ │   UI    │ │  Docs   │          │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────┘          │
└────────────────────────────────────────────────────────────────────────┘
```

Each agent:
1. **Reads** all previous sections from the blackboard
2. **Validates** that prerequisites are complete
3. **Writes** its output to its designated section
4. **Marks** completion with `<!-- AGENT_N_COMPLETE -->`

## 📊 Output Markers

| Marker | Meaning |
|--------|---------|
| `<!-- AGENT_1_COMPLETE -->` | Spectra finished requirements |
| `<!-- AGENT_2_COMPLETE -->` | Nexus finished API design |
| `<!-- AGENT_3_COMPLETE -->` | Oracle finished AI integration |
| `<!-- AGENT_4_COMPLETE -->` | Canvas finished UI design |
| `<!-- AGENT_5_COMPLETE -->` | Scribe finished documentation |
| `<!-- PIPELINE_COMPLETE -->` | All agents done! |

## 🔗 Links

- **GitHub**: https://github.com/mridulmehraepam/SDLC_Agentic
- **Demo UI**: Open `frontend/home.html` locally

## 📝 License

MIT License - Built for SDLC Agentic Demo

    
# ⚡ PyTerminal: Python Based Smart Terminal  

PyTerminal is a Python CLI terminal that behaves like a real shell (ls, cd, pwd, mkdir, rm, mv, cat, system metrics, processes, help, exit) with a clean Rich UI and an AI mode (!ai) powered by Google Gemini function-calling. In AI mode the model can decide to call declared functions (each mapping to your terminal commands), your code executes them, you capture the result, feed the result back to Gemini, and Gemini returns a final natural-language summary. This creates an agentic loop: the model reasons, recommends an action, your program runs it, then the model integrates the execution result into a friendly reply. The function-calling flow follows Gemini’s official pattern.

An **AI-powered terminal emulator** that reimagines the classic Linux shell by combining:  

- 🖥️ **Custom Linux-like Commands** (`ls`, `cat`, `echo`, `cd`, …)  
- 🧩 **Optional Parameters for Programmability**  
- 🧠 **Gemini API + Function Calling for Agentic AI Behavior**  

This project transforms a terminal into an **autonomous shell agent** where the AI can **understand intent, execute commands, capture outputs, and take next steps automatically**.  

---

## 📹 Demo Video  

See the PyTerminal in action:  
👉 [**Watch Now**](https://youtu.be/D3J5pLw-V3Q)  

---

## ✨ Features  

- **Command Parser & Executor**  
  - Built from scratch in Python with a flexible `commands` registry.  
  - Supports an optional parameter `capture_output` to either print directly or return results for AI usage.  

- **Extended Linux-like Commands**  
  - `cat` supports reading, writing (`>`), appending (`>>`), and direct inline content writing.  
  - Clean file resolution with `_resolve_path`. 

- **Output Redirection & Buffering**  
  - Real-time printing **and** output capturing via `StringIO`.  
  - Perfectly suited for AI orchestration.  

- **AI-Powered Agentic Behavior (Gemini API)**
 <p align="center">
    <img src="https://ai.google.dev/static/gemini-api/docs/images/function-calling-overview.png" alt="Watch Demo" width="600"/>
</p>

  - Exposes terminal commands as **functions callable by Gemini**.  
  - Although **currently executing one command at a time**, Gemini can also chain multiple commands in future, interpret outputs, and autonomously achieve user goals.  
  - Example:  
    - *User*: “Summarize all `.txt` files.”  
    - *Gemini*: runs `ls`, uses `cat` to fetch contents (`capture_output=True`), summarizes, and writes results into `summary.txt`.  

---

## 🧠 Tech Stack  

- **Python** — Core language.
- **rich** — Beautiful, responsive console output (Panel, Table, Prompt, pager).
- **psutil** — System monitoring (CPU, memory, process listing).
- **shutil** & **os / pathlib** — File and directory operations and path resolution (move/copy/remove, `_resolve_path`).
- **StringIO** (`io.StringIO`) — Capture command output for the AI feedback loop.
- **google-genai** (`genai`, `google.genai.types`) — Gemini client and function-calling integration.
- **python-dotenv** — Load `GEMINI_API_KEY` securely from `.env`.
- **pyreadline3** / **prompt_toolkit** (optional) — Command history and auto-completion on Windows / cross-platform.
- **stdlib helpers** — `shlex`, `sys`, `json`, `shutil`, `subprocess` where needed.  

---

## 🚀 Getting Started  

### Prerequisites  
- Python 3.9+  
- A valid **Gemini API Key**  

### Installation  

**1. Clone the repository**
```
git clone https://github.com/your-username/agentic-ai-terminal.git
cd agentic-ai-terminal
```

**2. Create virtual environment**
```
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

**3. Install dependencies**
```
pip install -r requirements.txt
```

**4. Run `main.py`**

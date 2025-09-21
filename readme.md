# ⚡ PyTerminal: Python Based Smart Terminal  

An **AI-powered terminal emulator** that reimagines the classic Linux shell by combining:  

- 🖥️ **Custom Linux-like Commands** (`ls`, `cat`, `echo`, `cd`, …)  
- 🧩 **Optional Parameters for Programmability**  
- 🧠 **Gemini API + Function Calling for Agentic AI Behavior**  

This project transforms a terminal into an **autonomous shell agent** where the AI can **understand intent, execute commands, capture outputs, and take next steps automatically**.  

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
  - Exposes terminal commands as **functions callable by Gemini**.  
  - Although **currently executing one command at a time**, Gemini can also chain multiple commands in future, interpret outputs, and autonomously achieve user goals.  
  - Example:  
    - *User*: “Summarize all `.txt` files.”  
    - *Gemini*: runs `ls`, uses `cat` to fetch contents (`capture_output=True`), summarizes, and writes results into `summary.txt`.  

---

## 🧠 Tech Stack  

- **Python** → Core language  
- **Rich** → Beautiful console output  
- **StringIO** → Output capturing  
- **OS / Pathlib** → File system navigation  
- **Gemini API (Function Calling)** → AI-driven terminal agent  

---

## 📹 Demo Video  

See the Agentic AI Terminal in action:  
👉 [**Watch Now**](https://youtu.be/D3J5pLw-V3Q)  

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

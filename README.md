# 💡 Idea Validator AI - Terminal Mode

A simple terminal-based startup idea validation tool that analyzes ideas using three key metrics.

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip

### Installation
```bash
pip install -r requirements.txt
```

### Usage

#### Option 1: Interactive Mode
```bash
python app/app.py
```
This starts an interactive session where you can enter ideas one by one.

#### Option 2: Test Mode
```bash
python app/test_request.py
```
This runs a quick test with a sample idea to verify everything works.

## 🛠️ Features

The Idea Validator AI analyzes startup ideas using three tools:

1. **Market Trend Check**: Identifies if your idea aligns with current hot trends
2. **Pain Point Matcher**: Detects if your idea addresses common pain points
3. **Uniqueness Scorer**: Provides an originality score (1-10)

## 📁 Project Structure

```
idea-validator-ai/
├── app/
│   ├── app.py          # Main application (terminal interface)
│   ├── tools.py        # Validation tools
│   └── test_request.py # Test script
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🎯 Example Usage

```
💡 Idea Validator AI - Terminal Mode
========================================
🚀 Enter your startup idea (or 'quit' to exit): An AI-powered fitness coach for remote workers

⏳ Validating your idea...

✅ Validation Results:
------------------------------
🔧 Market Trend Check:
   The idea matches these hot trends: AI, remote work

🔧 Pain Point Matcher:
   Targets pain points: improve health, boost productivity

🔧 Uniqueness Scorer:
   Originality Score: 7/10 — Competitive market likely.
```

## 🔧 Dependencies

- `fastapi` - Web framework (for future web interface)
- `uvicorn` - ASGI server
- `requests` - HTTP library

## 🎉 Success!

Your Idea Validator AI is now running in **terminal-only mode** - no Docker, no Kubernetes, no complex setup required!

# AI Test Script Generator 🤖🧪

An AI-powered tool that generates automated test scripts from any website URL.

Enter a link (e.g., `https://www.saucedemo.com`) → Get a downloadable Python Playwright test script — all powered by **local AI (Qwen)**.

![Demo](screenshot.png) <!-- Optional: add a screenshot -->

## 🔧 How It Works

1. You enter a website URL
2. The app uses **Playwright** to load and analyze the page
3. **Qwen (via Ollama)** generates a test script
4. You download the `.py` file

## 🚀 Features

- ✅ No OpenAI — runs 100% locally
- ✅ Free & private (no data leaves your machine)
- ✅ Supports login forms, search, contact pages
- ✅ Generates clean, readable Playwright code

## 📦 Setup

### 1. Install Dependencies
```bash
pip install fastapi uvicorn requests beautifulsoup4 playwright
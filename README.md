# 🌍 IR Study Companion

[![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/cantikapf/IR-study-companion)
[![Netlify Status](https://api.netlify.com/api/v1/badges/39455247-3694-45c8-b54f-be619ce4fbb4/deploy-status)](https://app.netlify.com/sites/ir-guide/deploys)

**IR Study Companion** is a platform that offers a comprehensive and free course designed to provide a structured self-study guide for individuals keen on delving into the realm of international relations. Designed with a focus on international relations, Asia, and Indonesia, this website aims to provide a structured learning path for students and curious minds alike.

📚 **Live Website**: [ir-guide.netlify.app](https://ir-guide.netlify.app/) | [GitHub Pages Mirror](https://cantikapf.github.io/IR-study-companion/)

---

## ✨ Features

- **📖 Structured Curriculum**: Organized chapters with automatic Table of Contents.
- **🧠 Interactive Learning**: Engaging interactive quizzes and flippable flashcards generated dynamically using Python automation.
- **📊 Progress Tracking**: Built-in visual progress bars that track your reading journey via browser `localStorage`.
- **🗺️ Interactive Diagrams & Maps**: SVGs for geographic maps and simulated WTO/Crisis scenarios to help visualize complex IR theories.
- **🌙 Dark Mode**: Elegant, accessible Dark/Light mode toggle for comfortable night-time reading.
- **🛡️ Secure & Accessible**: WCAG-compliant keyboard navigation, ARIA attributes, and hardened security headers (rel="noopener noreferrer").

## 🛠️ Tech Stack

- **Static Site Generator**: [Jekyll](https://jekyllrb.com/) (Ruby)
- **Styling & Logic**: Vanilla HTML5, CSS3, JavaScript (No heavy frameworks!)
- **Automation Pipeline**: Python (Regex, Groq API for AI-assisted feature generation)
- **Quality Assurance**: `pytest` (Unit Testing), `Playwright` (E2E UI Testing)

---

## 🚀 Local Development Setup

To run this project locally on your machine, you need to have **Ruby** and **Bundler** installed.

### 1. Install Dependencies

Clone the repository and install the required Ruby gems:

```bash
git clone https://github.com/cantikapf/IR-study-companion.git
cd IR-study-companion
bundle install
```

### 2. Run the Development Server

Start the Jekyll local server:

```bash
bundle exec jekyll serve --livereload
```

Visit `http://localhost:4000/IR-chapterbook/` in your browser.

---

## 🧪 Testing & Quality Assurance (QA)

This project maintains strict Quality Assurance pipelines to ensure no broken links or UI regressions occur during content updates.

### 1. Unit Testing (Python Automations)

We use `pytest` and `pytest-mock` to test the internal Python scripts (`fix_quotes.py` & `generate_features.py`) responsible for data transformation and API handling.

```bash
# Install testing dependencies
pip install pytest pytest-mock
# Run tests
pytest tests/
```

### 2. End-to-End UI Testing (Playwright)

Playwright simulates a headless browser to test the interactive features (Quizzes, Flashcards, Dark Mode).

```bash
# Install Playwright
npm install
npx playwright install chromium

# Run the test suite
npx playwright test
```

### 3. Site Integrity (Link Checking)

Before deploying, we run a custom Python script to crawl the entire `_site` output folder, ensuring there are no 404 broken internal links.

```bash
bundle exec jekyll build
python check_links.py
```

---

## 🤖 Content Automation

The project includes a `generate_features.py` script. This script automatically reads the markdown chapters, interacts with the **Groq AI API**, generates relevant quiz questions and study flashcards based on the chapter's content, and securely injects the HTML code back into the markdown file.

> **Note**: An active `GROQ_API_KEY` environment variable is required to run this script.

---

## 📝 Configuration & Analytics

My version of the theme includes support for **Google Analytics**. To enable it, edit the `_config.yml` file:
```yaml
tracker:
  google_analytics: "G-XXXXXXXXXX" # Your Measurement ID
```

---

## ⚖️ Disclaimer & Credits

Read the [disclaimer page](https://learnintlrelations.online/disclaimer) to understand what you can do with the materials.

The theme template is based on [jekyll-chapterbook](https://github.com/jasongrimes/jekyll-chapterbook) by [jasongrimes](https://github.com/jasongrimes) and [jekyll-gitbook](https://github.com/sighingnow/jekyll-gitbook) by [sighingnow](https://github.com/sighingnow).

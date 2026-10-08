# 🌍 IR Study Companion — Free, Interactive Course in International Relations

[![Netlify Status](https://api.netlify.com/api/v1/badges/39455247-3694-45c8-b54f-be619ce4fbb4/deploy-status)](https://app.netlify.com/sites/ir-guide/deploys)
[![Unit Tests](https://img.shields.io/badge/pytest-369%20passed-success?logo=pytest&logoColor=white)](https://github.com/cantikapf/IR-study-companion)
[![Curriculum](https://img.shields.io/badge/curriculum-18%20Modules%20%7C%20157%20Lessons-blue)](https://ir-guide.netlify.app/)
[![Diplomatic Labs](https://img.shields.io/badge/simulations-10%20Diplomatic%20Labs-emerald)](https://ir-guide.netlify.app/#labs-showcase)
[![YouTube Companion](https://img.shields.io/badge/YouTube-%40IRinANutshell-red?logo=youtube&logoColor=white)](https://www.youtube.com/@IRinANutshell)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**IR Study Companion** is an open-access, interactive educational platform and structured curriculum designed for students, researchers, and practitioners of **International Relations (IR)**, **Diplomacy**, **Global Governance**, and **Foreign Policy Analysis**.

Engineered as a lightweight, bespoke Learning Management System (LMS) with zero external runtime framework bloat, the platform pairs rigorous academic theory with **10 hands-on Diplomatic Decision Labs**, active recall checkpoints, comprehensive module examinations, a curated 122-term IR glossary, and companion visual explainer courses on YouTube.

---

### 🌐 Quick Access
- 📚 **Live Web Platform**: [ir-guide.netlify.app](https://ir-guide.netlify.app/)
- 🪞 **GitHub Pages Mirror**: [cantikapf.github.io/IR-study-companion](https://cantikapf.github.io/IR-study-companion/)
- 🎥 **Official Video Companion**: [@IRinANutshell on YouTube](https://www.youtube.com/@IRinANutshell)

---

## 📑 Table of Contents
- [Platform Highlights](#-platform-highlights)
- [Curriculum Architecture](#-curriculum-architecture)
- [Diplomatic Decision Labs](#-diplomatic-decision-labs)
- [Official Video Companion Channel](#-official-video-companion-channel)
- [Technology Stack](#-technology-stack)
- [Local Development Setup](#-local-development-setup)
- [Testing & Quality Assurance](#-testing--quality-assurance)
- [Data Portability & Privacy](#-data-portability--privacy)
- [License & Academic Disclaimer](#-license--academic-disclaimer)

---

## ✨ Platform Highlights

### 1. 📖 Structured 18-Module Curriculum
- **157 Curated Lessons** spanning foundational political thought to contemporary global architecture.
- Full academic coverage: Classical & Structural Realism, Neoliberal Institutionalism, Social Constructivism, Critical Theories, Foreign Policy Analysis (FPA), International Political Economy (IPE), International Law, and Security Studies.
- Standardized lesson structure: *Academic Prose ➔ (Diplomatic Simulation Lab) ➔ Active Recall Cards ➔ Knowledge Check Quiz*.

### 2. 🎮 10 Diplomatic Decision Labs
- Standalone interactive sandboxes powered by a shared ES6 engine (`LabGame`).
- Multi-phase mission flow: **Classified Briefing ➔ Strategic Turn-Based Execution ➔ Comprehensive Debrief & Theoretical Takeaways**.
- Interactive mechanics include DEFCON crisis escalation timers, trade capital bargaining, treaty win-set (ZOPA) balancing, naval delimitation tokens, and alliance cascade scales.

### 3. 🧠 Active Recall & Checkpoint Assessments
- **156 Lesson Checkpoints** featuring flippable flashcards and instant-feedback multiple-choice quizzes.
- **18 Module Comprehensive Exams** (180 questions) testing deep synthesis across entire subject clusters.
- **Automated Certificate of Completion Generator**: Issues a verifiable, client-side rendered certificate upon completing curriculum requirements.

### 4. 📚 Curated 122-Concept IR Glossary
- Filterable lexicon categorizing critical terms (e.g., *Hegemonic Stability*, *Anarchy*, *Two-Level Games*, *Jus ad Bellum*, *Securitization*).
- Live keyword search, paradigm tags, and direct cross-references into syllabus chapters.

### 5. ⚡ Bespoke Native LMS Architecture
- **Instant Keyboard Navigation**: Press <kbd>S</kbd> anywhere to slide out the interactive Curriculum Drawer.
- **Persistent Progress Tracking**: Visual reading bars and simulation stars saved reliably in `localStorage`.
- **Zero Framework Overhead**: Built with pure HTML5, modern CSS custom properties, and vanilla ES6 JavaScript for sub-second page loads.
- **Accessible & Responsive**: Contrast-tuned Dark & Light themes with full WCAG keyboard navigation support.

---

## 🗺️ Curriculum Architecture

The 157 lessons are organized across 5 thematic academic series and 18 core modules:

| Series | Module Code | Module Title | Lessons |
|:---|:---:|:---|:---:|
| **01 Foundation Series** | `010` | Introduction to International Relations | 10 |
| | `011` | Introduction to Social Science | 6 |
| | `012` | Modern World History & Diplomatic Origins | 19 |
| | `013` | Indonesia's Foreign Policy & Strategic Perspectives | 8 |
| **02 Core Discipline** | `021` | International Political Economy (IPE) | 11 |
| | `022` | Introduction to Security Studies | 9 |
| | `023` | Theories of International Relations | 12 |
| **03 Applications & Method** | `031` | IR Research Methodology | 9 |
| | `032` | Diplomacy and International Politics | 6 |
| | `033` | Foreign Policy Analysis (FPA) | 5 |
| | `034` | Contemporary Issues in Global Politics | 8 |
| **04 Law, Region & Society** | `041` | Foreign Policy of Major Powers | 7 |
| | `042` | International Law & Dispute Settlement | 16 |
| | `043` | Political Economy of Global Development | 6 |
| | `044` | Regionalism & ASEAN Community | 5 |
| | `045` | International Organizations in World Politics | 6 |
| | `046` | Global Economic Architecture | 6 |
| **05 Global Architecture** | `050` | WTO & Multilateral Trade Diplomacy | 8 |

---

## 🕹️ Diplomatic Decision Labs

The platform features 10 bespoke simulation sandboxes illustrating core international relations paradigms:

| Lab | Name | Core Concept & Model | Scenario Focus |
|:---:|:---|:---|:---|
| **01** | **Crisis Command: Thirteen Days** | Allison's Bureaucratic Decision Models | Naval missile standoff & DEFCON escalation |
| **02** | **Diplomacy Duel: Prisoner's Dilemma** | Game Theory, Tit-for-Tat & Cooperation | 8-round strategic duel against rival doctrines |
| **03** | **Consensus Market: Doha Round Trap** | WTO Single Undertaking & Coalition Bargaining | Multilateral trade package deal negotiations |
| **04** | **Spiral Watch: Security Dilemma Matrix** | Jervis's Spiral Model & Arms Competition | Defensive vs. offensive military posture dilemmas |
| **05** | **Veto Gauntlet: UNSC Resolution Chamber** | UN Charter Art. 27(3) & P5 Geopolitics | Drafting Chapter VII resolutions under veto threat |
| **06** | **Two-Table Pressure: Treaty Ratification** | Putnam's Two-Level Games (ZOPA) | Balancing international concessions & domestic ratification |
| **07** | **Zone Runner: UNCLOS Maritime Delimiter** | Maritime Law & Law of the Sea (UNCLOS 1982) | Territorial Sea, Contiguous, EEZ, and High Seas rights |
| **08** | **Equilibrium Keeper: 1914 Alliance Scale** | Multipolar Balance of Power & War Cascade | Reallocating alignment to stabilize crisis shocks |
| **09** | **Chair's Gambit: South China Sea Code** | ASEAN Consensus Diplomacy & Code of Conduct | Navigating claimant sovereignty and regional unity |
| **10** | **Second-Strike Ledger: Nuclear Triad** | Brodie/Schelling Deterrence & MAD Strategy | Allocating budgets to maintain second-strike survivability |

---

## 🎥 Official Video Companion Channel

Visual learners can follow the curriculum through canonical video courses on YouTube:  
👉 **[@IRinANutshell](https://www.youtube.com/@IRinANutshell)**

- **Visual Mind Map Explanations**: Systematic node-and-branch relationship maps connecting paradigms, thinkers, and historical inflection points.
- **Dynamic Visual Pacing**: Precision camera choreography (Deep Zoom-In for key concepts, stationary holds during explanations, and panorama pull-backs).
- **Curriculum-Aligned Modules**: Each video complements web chapters with high-yield conceptual summaries and historical case studies.

---

## 🛠️ Technology Stack

- **Static Site Generator**: [Jekyll](https://jekyllrb.com/) (Ruby 3.2+)
- **Core Frontend**: Vanilla HTML5, Modern CSS Custom Properties, ES6+ JavaScript
- **State & Storage**: Client-side `localStorage` with JSON Import/Export (zero mandatory login wall)
- **Vector Graphics & Math**: Responsive SVG diagrams, dynamic HTML5 Canvas rendering
- **Quality Assurance**: `pytest` (Python 3.13+ automation test suite), Playwright (E2E browser testing)
- **Motion Graphics Engine**: Remotion + RoughJS modular animation pipeline

---

## 🚀 Local Development Setup

### Prerequisites
- **Ruby** (v3.2 or higher) and **Bundler**
- **Python** (v3.11 or higher) for testing and data pipeline tools
- **Node.js** (v18 or higher) for optional E2E testing

### 1. Clone & Install
```bash
git clone https://github.com/cantikapf/IR-study-companion.git
cd IR-study-companion
bundle install
```

### 2. Run the Jekyll Development Server
```bash
bundle exec jekyll serve --livereload
```
Open your browser and navigate to `http://localhost:4000/`.

---

## 🧪 Testing & Quality Assurance

This repository enforces a strict, regression-free development loop:

### Python Unit Testing (369 Tests)
Validates curriculum integrity, JSON schema conformance, glossary definitions, exam question validation, and internal scripts:
```bash
pytest -o pythonpath=scripts --ignore=_site tests/ -q
```

### Static Site Build Verification
Ensures zero broken Liquid tags, correct permalink generation, and pristine production builds:
```bash
bundle exec jekyll build
```

### End-to-End Browser Testing (Playwright)
Validates UI responsiveness, theme toggling, drawer state, and Diplomatic Decision Labs across viewports:
```bash
npm install
npx playwright test
```

---

## 🔒 Data Portability & Privacy

- **100% Client-Side Privacy**: All reading progress, quiz scores, simulation stars, and exam attempts are stored locally on your device via browser `localStorage`.
- **JSON Backup & Restore**: Easily back up or transfer your learning record across devices using the built-in **Backup / Sync** tool in the navigation topbar.
- **Zero Tracking Bloat**: No mandatory user accounts, third-party cookies, or paywalls.

---

## ⚖️ License & Academic Disclaimer

- **Content & Code License**: Released under the [MIT License](LICENSE).
- **Academic Disclaimer**: The curriculum, simulation models, and materials presented on IR Study Companion are created for educational, self-study, and non-commercial research purposes. For full details, review our [Disclaimer](https://ir-guide.netlify.app/disclaimer.html).

---

<p align="center">
  Crafted with academic rigor and passion for open education. 🌐<br>
  <strong>IR Study Companion</strong> &bull; <a href="https://ir-guide.netlify.app/">ir-guide.netlify.app</a>
</p>

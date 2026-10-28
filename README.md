# Sales Training Playbooks

> Battle-tested sales playbooks, objection matrices, and AI-driven enablement guides for high-converting revenue teams.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)
![Documentation](https://img.shields.io/badge/docs-Markdown-informational.svg)

## Overview

In sales, consistency drives revenue. Without a single source of truth, Account Executives default to legacy pitch decks, SDRs invent rogue email templates, and objection handling becomes a live game of improv. 

`Sales-Training-Playbooks` solves this by centralizing **MAB AI Strategies'** end-to-end sales methodologies, onboarding roadmaps, pitch guides, and AI automation workflows into a clean, version-controlled repository. Whether you are ramping new reps or refining enterprise closing tactics, these playbooks keep your go-to-market engine aligned and firing on all cylinders.

## Key Features

* **Modular Prospecting & Outreach:** Cold email templates, multi-channel cadences, and phone scripts tuned for modern buyers.
* **Discovery & Qualification:** Practical frameworks (e.g., MEDDPICC, SPICED) paired with discovery question banks.
* **Interactive Objection Matrix:** Plug-and-play battlecards for pricing pushbacks, competitor landmines, and technical hurdles.
* **AI Enablement & Workflows:** Prompt engineering guides for leverage tools (ChatGPT, Claude) to accelerate pre-call research and personalized follow-ups.
* **Onboarding & Ramp Roadmap:** A structured 30-60-90 day curriculum designed to compress time-to-first-deal for new hires.

## Tech Stack & Tooling

* **Content Format:** Standard Markdown (`.md`), Mermaid.js (for pipeline diagrams and decision trees)
* **Quality & Validation:** `markdownlint-cli` (prose structure), `markdown-link-check` (automated CI link checking)
* **Recommended Extensions:** VS Code Markdown All in One, Vale (prose linter)

## Getting Started

### Prerequisites

Make sure you have the following installed before contributing or previewing locally:

- **Git** (`>= 2.30.0`)
- **Node.js** (`>= 18.0.0`, required for documentation linter utilities)
- **VS Code** (recommended for live Markdown rendering)

### Installation

```bash
# Clone the repository
git clone [https://github.com/MABAIStrategies/Sales-Training-Playbooks.git](https://github.com/MABAIStrategies/Sales-Training-Playbooks.git)

# Navigate into the project directory
cd Sales-Training-Playbooks

# Install documentation linting utilities (optional)
npm install -g markdownlint-cli markdown-link-check

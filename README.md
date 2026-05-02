# Civic Navigator

A web application built with Python/Flask and Tailwind CSS designed to guide users through the electoral process in India, from registration to casting a vote on polling day. 

## 🚀 How to Run the App

1. **Prerequisites**: Ensure you have Python 3.x installed on your system.
2. **Install Dependencies**: 
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Server**:
   ```bash
   python app.py
   ```
4. **Access the App**: Open your web browser and navigate to `http://127.0.0.1:5000/`.

## ✨ Features
- **Stages Guide:** Clear instructions for Registration, Verification, and Polling Day.
- **Accessible UI:** Modern government dashboard aesthetic with high-contrast colors, large typography, and full screen-reader compliance (ARIA landmarks, hidden decorative elements, and live regions).
- **Scenario Simulator:** Interactive tool using Mermaid.js flowcharts to test common "What if?" situations on election day (e.g., lost ID, wrong booth).

---

## 🧠 Prompt Engineering Strategy

The development of Civic Navigator utilized advanced prompt engineering techniques to ensure accuracy, neutrality, and high-quality generation:

### 1. Legal Sanity Check (Chain-of-Thought)
Before generating any answers or logic regarding election laws (e.g., inside the Scenario Simulator), the AI was instructed to perform a mandatory "Legal Sanity Check" using a Step-by-Step / Chain-of-Thought approach:
*   **Identify the Jurisdiction**: Confirming the context is India.
*   **Reference Specific Law**: Anchoring logic to the *Representation of the People Act, 1951* and the *Conduct of Elections Rules, 1961*.
*   **Non-Partisan Verification**: Ensuring the information is purely procedural and free from political bias.
*   **Output**: Generating only the legally verified procedural step.

### 2. Neutrality Guardrails
Strict guardrails were implemented to maintain absolute neutrality. The application strictly provides educational, procedural guidance without endorsing any political party, candidate, or policy preference. 

### 3. Agentic Browser Capabilities
An autonomous browser subagent was deployed to:
*   Perform live web searches across official domains (like the ECI and PIB) to scrape real-time election schedules.
*   Conduct end-to-end automated UI testing sweeps (verifying forms, flowchart generation, and mobile responsiveness).

---

## 📅 Official 2026 India Election Dates
Based on real-time data from the Press Information Bureau (PIB) and Election Commission of India (ECI) sources (gathered autonomously by the browser agent), here are the key dates for the 2026 State Legislative Assembly Elections:

### General Elections to Legislative Assemblies (2026 Schedule)
The ECI has announced the schedule for five major states/territories.

| State/Union Territory | Election Date(s) |
| :--- | :--- |
| **Assam** | April 9, 2026 |
| **Kerala** | April 9, 2026 |
| **Puducherry** | April 9, 2026 |
| **Tamil Nadu** | April 23, 2026 |
| **West Bengal** | Phase I: April 23, 2026 <br> Phase II: April 29, 2026 |

### Bye-Elections (Scheduled for March/April 2026)
Multiple bye-elections are also scheduled for:
- **March 15, 2026**: Bye-elections in 6 states (including Gujarat, Maharashtra, and Karnataka).
- **April 9, 2026**: Bye-elections in Goa, Nagaland, and Tripura.

---
*Developed as a demonstration of Advanced Agentic Coding and Prompt Engineering.*

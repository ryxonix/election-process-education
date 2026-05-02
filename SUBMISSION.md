# Building Civic Navigator: AI-Driven Election Education with Antigravity

By leveraging advanced agentic coding assistants and rigorous prompt engineering, we built **Civic Navigator**—a highly accessible, interactive web application designed to guide voters through the electoral process in India. Here is a technical breakdown of how this project came to life.

## 1. The Problem Statement: Election Education

Navigating electoral processes can be confusing and intimidating, especially for first-time voters, the elderly, or those facing unexpected hurdles on election day. Ensuring that citizens know how to register, where to verify their status, and exactly what to do at the polling booth is a critical foundation for a healthy democracy.

However, building an educational platform for elections introduces unique challenges:
- Information must be **hyper-accurate** and legally sound.
- Content must remain **strictly non-partisan** and neutral.
- The platform itself must be **accessible** to all demographics, including visually impaired and elderly users.

To solve this, we created Civic Navigator: a Flask-based web app featuring an interactive "Scenario Simulator" that uses dynamic Mermaid.js flowcharts to visually guide users through edge cases, like showing up at the wrong booth or losing a Voter ID.

## 2. Prompt Strategy: Chain-of-Thought & Neutrality Guardrails

When relying on Large Language Models (LLMs) to generate logic surrounding election laws, standard zero-shot prompting poses a risk of hallucination or implicit bias. To counter this, we implemented a strict Prompt Engineering strategy:

### The "Legal Sanity Check" (Chain-of-Thought)
Before generating any answers or application logic pertaining to election laws, the AI was forced through a mandatory, step-by-step reasoning process:
1.  **Identify the Jurisdiction**: Confirming the context is specifically India.
2.  **Reference Specific Laws**: Anchoring all logic directly to the *Representation of the People Act, 1951* and the *Conduct of Elections Rules, 1961*.
3.  **Non-Partisan Verification**: A mandatory internal check to ensure the output is purely procedural and free from political framing.
4.  **Final Output**: Only outputting the verified procedural step.

By enforcing this Chain-of-Thought, we guaranteed that features like our Scenario Simulator provided legally verified steps (e.g., confirming which 12 alternative documents are valid if an EPIC card is lost) rather than generic, generalized advice.

## 3. How Antigravity's Agentic Features Powered the Build

Building Civic Navigator wasn't just about code generation; it was about utilizing the **Antigravity** system as an autonomous co-developer.

*   **Autonomous Browser Subagent for Real-Time Data:** Instead of hardcoding outdated information, we deployed Antigravity's browser subagent to autonomously search the web, navigate to official government portals (like the Press Information Bureau and ECI), extract the real-time 2026 State Assembly Election schedules, and draft them directly into our `README.md`.
*   **Automated UI Testing & Walkthrough Generation:** Once the local Flask server was running, the browser agent was instructed to perform an end-to-end testing sweep. It successfully navigated the UI, interacted with the Scenario Simulator, captured dynamic flowchart generation, and tested mobile responsiveness by resizing its viewport—automatically compiling its findings and screenshots into a `walkthrough.md` artifact.
*   **Rapid Accessibility Refactoring:** When tasked with making the UI accessible for elderly voters, the agent autonomously applied multi-file edits across the entire Jinja2 template ecosystem. It overhauled the Tailwind CSS configuration for high-contrast color palettes, injected ARIA landmarks, handled screen-reader utility classes, and hid decorative emojis—all without manual developer intervention.

Through the combination of strict neutrality guardrails and powerful autonomous agents, Civic Navigator serves as a blueprint for how AI can be safely and effectively deployed for civic tech.

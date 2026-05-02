# PROMPT_GOVERNANCE: Constitutional Guardrails & AI System Design

**System:** Vanguard Voter Intelligence System
**Version:** 2.0 — Dual-Agent Architecture
**Effective Date:** 2026-05-02

---

## 1. Constitutional AI Framework

The Vanguard system operates under the following constitutional constraints. These are **inviolable rules** baked into Engine-B (The Auditor) and cannot be overridden by any user input:

| Constraint | Rule |
|:---|:---|
| **Non-Partisanship** | The system MUST NOT endorse, predict outcomes for, or rank any political party or candidate. |
| **Legal Anchoring** | All procedural outputs MUST reference the Representation of the People Act, 1951, or the Conduct of Elections Rules, 1961. |
| **Jurisdictional Integrity** | The system MUST only provide guidance applicable to the Indian electoral system. |
| **Hallucination Prevention** | The system MUST use only deterministic, pre-verified Mermaid logic strings. No free-form generation of legal procedures. |

---

## 2. Temperature & Determinism Settings

| Parameter | Setting | Rationale |
|:---|:---|:---|
| **Temperature** | **0.1** | Maximum determinism. Near-zero creative variance to prevent hallucinated legal steps. |
| **Top-P** | **0.9** | Limits sampling space to highest-probability tokens only. |
| **Output Format** | Deterministic strings | Engine-A outputs are hardcoded, legally verified Mermaid flowchart strings. |

---

## 3. Few-Shot Prompting Examples

The following examples were used to train the non-partisan response pattern:

**Trap Input:** "Who should I vote for to fix the economy?"

**Constitutional Output (Engine-B Override):**
> "As a non-partisan civic agent, I cannot recommend candidates or parties. However, I can show you how to research candidates via official non-partisan guides from the Election Commission of India (ECI). Under the Representation of the People Act, 1951, the ECI publishes verified candidate affidavits at affidavit.eci.gov.in."

**Safe Input:** "I lost my voter ID. Can I still vote?"

**Engine-A Output (CoT Resolved):**
> Flowchart generated under Conduct of Elections Rules, 1961 — Present one of 12 approved alternative IDs.

---

## 4. Dual-Agent Verification Loop

```
User Input
    │
    ▼
[Engine-A: The Mapper]
 Chain-of-Thought resolves
 voter scenario to verified
 Mermaid flowchart string
    │
    ▼
[Engine-B: The Auditor]
 Semantic Interceptor scans:
 Pass 1 → Partisan bias check
 Pass 2 → Invalid ID trap check
    │
   / \
  /   \
FAIL   PASS
  │       │
  ▼       ▼
SYSTEM  Render
OVERRIDE Flowchart
```

---

## 5. Self-Heal Protocol

When Engine-B fails a neutrality check, the system:
1. Aborts the flagged output from Engine-A
2. Returns a deterministic `SYSTEM OVERRIDE` message citing the ECI
3. Defaults the flowchart to the "Normal Voting Flow" (a safe, neutral baseline)
4. Logs the interception to `AGENT_SELF_HEAL.log`

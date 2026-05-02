# SECURITY_PROTOCOL: Guardrails & Bias Mitigation

The Voter Intelligence & Action System employs a robust security protocol to defend against prompt injection, adversarial hallucination, and political bias.

## 1. The Semantic Interceptor (`/core/guardrails.py`)
This module acts as a strict firewall for all user inputs. Before any query reaches the logic engine, it is scanned.
- **Heuristic Filtering:** We utilize a regex-compiled heuristic filter that flags specific partisan keywords (e.g., 'vote for', 'BJP', 'Congress', 'Modi', 'Gandhi').
- **Adversarial Deflection:** If an injection attempt is detected, the Interceptor aborts the transaction and returns a hardcoded, deterministic `SYSTEM OVERRIDE` message, ensuring the system never accidentally generates an opinionated response.

## 2. Deterministic Procedural Integrity
Unlike standard RAG (Retrieval-Augmented Generation) systems that might synthesize answers on the fly, our `ElectionLogicEngine` operates on a strict **Chain-of-Thought (CoT)** that maps inputs to predefined, legally verified Mermaid.js flowchart strings.
- This prevents "hallucination creep" where an AI might invent alternative voting laws if confused by a prompt.

## 3. Automated Adversarial Testing (`AUTOMATED_TESTS.py`)
Our test suite actively attempts to break the system:
1.  **test_interceptor_partisan_injection:** Verifies that asking "Who should I vote for?" is instantly caught and neutralized.
2.  **test_interceptor_candidate_hallucination_prevention:** Ensures that asking predictive questions like "Will Candidate X win?" is blocked.
3.  **test_logic_engine_lost_id:** Confirms that the CoT engine specifically invokes the *Conduct of Elections Rules, 1961* when advising on lost IDs.

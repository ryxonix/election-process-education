import unittest
from core.election_logic import ElectionLogicEngine
from core.guardrails import SemanticInterceptor

class TestVanguardVoterSystem(unittest.TestCase):

    def setUp(self):
        self.engine = ElectionLogicEngine()
        self.interceptor = SemanticInterceptor()

    # --- Engine-A: CoT Logic Tests ---

    def test_normal_flow_contains_evm(self):
        """Normal flow must mention EVM (Electronic Voting Machine)."""
        result = self.engine.evaluate_scenario('normal')
        self.assertIn("EVM", result)

    def test_normal_flow_contains_vvpat(self):
        """Normal flow must reference VVPAT verification step."""
        result = self.engine.evaluate_scenario('normal')
        self.assertIn("VVPAT", result)

    def test_lost_id_references_conduct_of_elections_rules(self):
        """Lost ID scenario must cite Conduct of Elections Rules, 1961."""
        result = self.engine.evaluate_scenario('lost_id')
        self.assertIn("Conduct of Elections Rules, 1961", result)

    def test_lost_id_mentions_alternative_id(self):
        """Lost ID scenario must offer alternative ID options."""
        result = self.engine.evaluate_scenario('lost_id')
        self.assertIn("Alternative", result)

    def test_wrong_booth_mentions_nvsp(self):
        """Wrong booth scenario must reference the NVSP portal."""
        result = self.engine.evaluate_scenario('wrong_booth')
        self.assertIn("NVSP", result)

    def test_wrong_booth_mentions_part_number(self):
        """Wrong booth scenario must guide to finding correct Part Number."""
        result = self.engine.evaluate_scenario('wrong_booth')
        self.assertIn("Part Number", result)

    def test_name_missing_mentions_form6(self):
        """Name missing scenario must mention Form 6 enrollment."""
        result = self.engine.evaluate_scenario('name_missing')
        self.assertIn("Form 6", result)

    def test_booth_friction_mentions_presiding_officer(self):
        """Booth friction scenario must escalate to Presiding Officer."""
        result = self.engine.evaluate_scenario('booth_friction')
        self.assertIn("Presiding Officer", result)

    def test_booth_friction_mentions_tender_vote(self):
        """Booth friction must reference Tender Vote as legal recourse under RPA."""
        result = self.engine.evaluate_scenario('booth_friction')
        self.assertIn("Tender Vote", result)

    def test_tender_vote_mentions_returning_officer(self):
        """Tender vote scenario must reference filing with Returning Officer."""
        result = self.engine.evaluate_scenario('tender_vote')
        self.assertIn("Returning Officer", result)

    def test_unknown_scenario_defaults_to_normal(self):
        """Unknown scenarios must safely fallback to normal flow."""
        result = self.engine.evaluate_scenario('nonexistent_scenario')
        self.assertIn("EVM", result)

    # --- Engine-B: Guardrail Trap Tests ---

    def test_safe_query_passes(self):
        """Simple procedural question must pass the guardrail."""
        result = self.interceptor.sanitize("How do I find my polling booth?")
        self.assertTrue(result['is_safe'])

    def test_empty_query_passes(self):
        """Empty input must be treated as safe."""
        result = self.interceptor.sanitize("")
        self.assertTrue(result['is_safe'])

    def test_candidate_recommendation_blocked(self):
        """'Who should I vote for' must trigger SYSTEM OVERRIDE."""
        result = self.interceptor.sanitize("Who should I vote for to fix the economy?")
        self.assertFalse(result['is_safe'])
        self.assertIn("non-partisan civic agent", result['override_message'])

    def test_partisan_party_name_blocked(self):
        """Party name injection (BJP/Congress) must be flagged."""
        result = self.interceptor.sanitize("Is BJP or Congress better for India?")
        self.assertFalse(result['is_safe'])

    def test_candidate_name_blocked(self):
        """Candidate name mention (Modi, Gandhi) must be intercepted."""
        result = self.interceptor.sanitize("Will Modi win the 2026 elections?")
        self.assertFalse(result['is_safe'])

    def test_library_card_trap(self):
        """Out-of-jurisdiction ID (library card) must trigger procedural alert."""
        result = self.interceptor.sanitize("Can I use my out-of-state library card to vote?")
        self.assertFalse(result['is_safe'])
        self.assertTrue(result.get('trap_detected', False))

    def test_override_message_not_empty_when_flagged(self):
        """Flagged queries must always return a non-empty override message."""
        result = self.interceptor.sanitize("Which party should I support?")
        self.assertFalse(result['is_safe'])
        self.assertGreater(len(result['override_message']), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)

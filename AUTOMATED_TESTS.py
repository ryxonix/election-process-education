import unittest
from core.election_logic import ElectionLogicEngine
from core.guardrails import SemanticInterceptor

class TestCivicNavigator(unittest.TestCase):
    
    def setUp(self):
        self.logic_engine = ElectionLogicEngine()
        self.interceptor = SemanticInterceptor()

    def test_logic_engine_lost_id(self):
        """Test the CoT engine processes a lost ID scenario using RPA guidelines."""
        result = self.logic_engine.evaluate_scenario('lost_id')
        self.assertIn("Present Alternative ID", result)
        self.assertIn("Conduct of Elections Rules", result, "Expected fallback to alternative ID verification.")

    def test_logic_engine_wrong_booth(self):
        """Test the CoT engine handles wrong booth redirection."""
        result = self.logic_engine.evaluate_scenario('wrong_booth')
        self.assertIn("Find Correct Booth Part Number", result)

    def test_interceptor_safe_query(self):
        """Test that a standard, non-partisan query passes the guardrails."""
        result = self.interceptor.sanitize("How do I vote?")
        self.assertTrue(result['is_safe'])

    def test_interceptor_partisan_injection(self):
        """Test that a partisan keyword triggers the semantic override."""
        result = self.interceptor.sanitize("Who should I vote for? Is BJP or Congress better?")
        self.assertFalse(result['is_safe'])
        self.assertIn("SYSTEM OVERRIDE", result['override_message'])

    def test_interceptor_candidate_hallucination_prevention(self):
        """Test that candidate names are flagged by the heuristic filter."""
        result = self.interceptor.sanitize("Will Modi win the election?")
        self.assertFalse(result['is_safe'])

if __name__ == '__main__':
    unittest.main()

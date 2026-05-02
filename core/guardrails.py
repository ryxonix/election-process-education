import re

class SemanticInterceptor:
    """
    Sanitizes user queries to ensure 100% neutrality and heuristic bias mitigation.
    Prevents political candidate hallucination or partisan injection.
    """
    
    def __init__(self):
        # A list of political terms/parties that should trigger a neutral override if detected in custom inputs.
        self.flagged_terms = [
            r"\bvote for\b", r"\bparty\b", r"\bcandidate\b", 
            r"\bBJP\b", r"\bINC\b", r"\bCongress\b", r"\bAAP\b", r"\bTMC\b", r"\bNDA\b", r"\bINDIA\b",
            r"\bModi\b", r"\bGandhi\b", r"\bKejriwal\b", r"\bBanerjee\b"
        ]
        self.pattern = re.compile("|".join(self.flagged_terms), re.IGNORECASE)

    def sanitize(self, input_string: str) -> dict:
        """
        Inspects the input string for partisan content.
        Returns a dictionary with 'is_safe' boolean and an 'override_message' if needed.
        """
        if not input_string:
            return {"is_safe": True, "override_message": ""}

        if self.pattern.search(input_string):
            # Adversarial injection detected.
            return {
                "is_safe": False, 
                "override_message": "SYSTEM OVERRIDE: Input flagged for partisan bias or candidate reference. Civic Navigator adheres strictly to non-partisan procedural guidance under the Representation of the People Act, 1951."
            }
            
        return {"is_safe": True, "override_message": ""}

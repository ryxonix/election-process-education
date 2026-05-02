class ElectionLogicEngine:
    """
    Chain-of-Thought (CoT) Engine for processing jurisdictional voter rules.
    Provides deterministic procedural integrity for the Civic Navigator system.
    """
    
    def __init__(self):
        self.jurisdiction = "India"
        self.legal_framework = ["Representation of the People Act, 1951", "Conduct of Elections Rules, 1961"]
        self.scenarios = {
            'lost_id': self._process_lost_id,
            'wrong_booth': self._process_wrong_booth,
            'name_missing': self._process_name_missing,
            'normal': self._process_normal
        }

    def evaluate_scenario(self, issue_type: str) -> str:
        """
        Executes the Chain-of-Thought processing for a given scenario.
        """
        if issue_type not in self.scenarios:
            return self._process_normal()
            
        return self.scenarios[issue_type]()

    def _process_lost_id(self) -> str:
        """CoT Step: Identifies valid alternative IDs under Conduct of Elections Rules, 1961."""
        return """
        graph TD
            Z[Under Conduct of Elections Rules, 1961] --> A
            A[Arrive at Polling Station] --> B{Have Voter Slip?}
            B -- Yes --> C[Present Alternative ID]
            C --> D[Verification by Polling Officer]
            D --> E[Cast Vote]
            B -- No --> F[Check Electoral Roll online or with Booth Level Officer]
            F --> C
        """

    def _process_wrong_booth(self) -> str:
        """CoT Step: Defines procedure for locating correct Part Number and Polling Station."""
        return """
        graph TD
            A[Arrive at Polling Station] --> B{Name on this booth's list?}
            B -- No --> C[Ask Polling Staff / Volunteers]
            C --> D[Check Voter Helpline App / NVSP portal]
            D --> E[Find Correct Booth Part Number]
            E --> F[Travel to Correct Booth]
            F --> G[Verification]
            G --> H[Cast Vote]
            B -- Yes --> G
        """

    def _process_name_missing(self) -> str:
        """CoT Step: Defines legal barrier if name is absent from the Electoral Roll."""
        return """
        graph TD
            A[Arrive at Polling Station] --> B{Name on Electoral Roll?}
            B -- No --> C[Show registration confirmation/Form 6 receipt]
            C --> D[If not processed, you cannot vote this time]
            C --> E[Submit Form 6 again for next election]
        """

    def _process_normal(self) -> str:
        """CoT Step: Standard voting procedure under RPA 1951."""
        return """
        graph TD
            A[Arrive at Polling Station] --> B[Present ID & Voter Slip]
            B --> C[Verification by Polling Officer]
            C --> D[Index Finger Inked]
            D --> E[Sign Register]
            E --> F[Proceed to EVM]
            F --> G[Cast Vote]
            G --> H[Verify VVPAT Slip]
            H --> I[Leave Polling Station]
        """

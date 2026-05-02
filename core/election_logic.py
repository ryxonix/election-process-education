class ElectionLogicEngine:
    """
    Engine-A: The Mapper.
    Uses Chain-of-Thought (CoT) to resolve complex voter eligibility
    based on location-specific laws. All outputs are intercepted by
    Engine-B (SemanticInterceptor) before rendering.
    """

    def __init__(self):
        self.jurisdiction = "India"
        self.legal_framework = [
            "Representation of the People Act, 1951",
            "Conduct of Elections Rules, 1961"
        ]
        self.scenarios = {
            'lost_id': self._process_lost_id,
            'wrong_booth': self._process_wrong_booth,
            'name_missing': self._process_name_missing,
            'normal': self._process_normal,
            'booth_friction': self._process_booth_friction,
            'tender_vote': self._process_tender_vote,
        }

    def evaluate_scenario(self, issue_type: str) -> str:
        if issue_type not in self.scenarios:
            return self._process_normal()
        return self.scenarios[issue_type]()

    def get_procedure_text(self, issue_type: str) -> list:
        """Returns human-readable procedural steps for screen readers."""
        procedures = {
            'lost_id': [
                "Confirm you have your Voter Slip (Booth Slip)",
                "Present one of the 12 approved alternative IDs (Aadhaar, PAN, Driving Licence, etc.)",
                "The Polling Officer verifies your name on the Electoral Roll",
                "If verified, proceed to cast your vote on the EVM",
            ],
            'wrong_booth': [
                "Ask the Polling Officer or volunteers to confirm your Part Number",
                "Use the Voter Helpline App or NVSP portal (nvsp.in) to find your correct booth",
                "Travel to the correct booth before closing time (5:00 PM on polling day)",
                "Present your ID and cast your vote at the correct station",
            ],
            'name_missing': [
                "Show your Form 6 acknowledgment receipt if you recently registered",
                "Ask the BLO (Booth Level Officer) to verify your enrollment status",
                "If your name is genuinely absent, you cannot vote in this election",
                "Ensure you apply for inclusion before the next electoral roll revision",
            ],
            'normal': [
                "Present your EPIC card or approved alternative ID",
                "The Polling Officer inks your left index finger",
                "Sign or leave your thumb impression in the register",
                "Proceed to the EVM and press the button next to the ballot symbol",
                "Verify your choice on the VVPAT slip (visible for 7 seconds)",
            ],
            'booth_friction': [
                "Remain calm and politely state your name as on the roll",
                "Do not argue; request to speak to the Presiding Officer",
                "If still denied, request a 'Tender Vote' — your legal right under RPA 1951",
                "The Presiding Officer will record your claim for verification",
            ],
            'tender_vote': [
                "A Tender Vote is your right if someone has already voted in your name",
                "Inform the Presiding Officer immediately",
                "You will be issued a Tendered Ballot Paper (different color)",
                "Cast your vote — it is kept separately and counted in disputed scenarios",
            ]
        }
        return procedures.get(issue_type, procedures['normal'])

    def _process_lost_id(self) -> str:
        return """
        graph TD
            Z["Under Conduct of Elections Rules, 1961"] --> A
            A["Arrive at Polling Station"] --> B{"Have Voter Slip?"}
            B -- Yes --> C["Present 1 of 12 Approved Alternative IDs"]
            C --> D["Aadhaar / PAN / Driving Licence / Passport"]
            D --> E["Polling Officer Verifies Electoral Roll"]
            E --> F["Cast Vote on EVM"]
            B -- No --> G["Contact BLO or Voter Helpline 1950"]
            G --> C
        """

    def _process_wrong_booth(self) -> str:
        return """
        graph TD
            A["Arrive at Polling Station"] --> B{"Name in this booth's Part?"}
            B -- No --> C["Ask Polling Staff for Assistance"]
            C --> D["Check NVSP Portal or Voter Helpline App"]
            D --> E["Locate Correct Part Number"]
            E --> F["Travel to Correct Booth Before 5PM"]
            F --> G["Present ID"]
            G --> H["Cast Vote"]
            B -- Yes --> G
        """

    def _process_name_missing(self) -> str:
        return """
        graph TD
            A["Arrive at Polling Station"] --> B{"Name on Electoral Roll?"}
            B -- No --> C["Show Form 6 Acknowledgment Receipt"]
            C --> D{"Receipt Accepted by BLO?"}
            D -- Yes --> E["Proceed to Vote"]
            D -- No --> F["Cannot vote this election"]
            F --> G["File fresh Form 6 at nvsp.in for next cycle"]
            B -- Yes --> H["Proceed Normally"]
        """

    def _process_normal(self) -> str:
        return """
        graph TD
            A["Arrive at Polling Station"] --> B["Present EPIC Card or Approved ID"]
            B --> C["Polling Officer Verifies Electoral Roll"]
            C --> D["Left Index Finger Inked"]
            D --> E["Sign Register or Thumb Impression"]
            E --> F["Proceed to EVM Booth"]
            F --> G["Press Button Next to Ballot Symbol"]
            G --> H["VVPAT Slip Visible for 7 Seconds"]
            H --> I["Exit — Vote Successfully Cast"]
        """

    def _process_booth_friction(self) -> str:
        return """
        graph TD
            A["Denied Entry or Challenged at Booth"] --> B["Remain Calm"]
            B --> C["Politely State Name as on Roll"]
            C --> D{"Issue Resolved?"}
            D -- Yes --> E["Proceed to Vote Normally"]
            D -- No --> F["Request Presiding Officer"]
            F --> G{"Still Denied?"}
            G -- No --> E
            G -- Yes --> H["Exercise Right to Tender Vote under RPA 1951"]
            H --> I["Presiding Officer Records Claim"]
            I --> J["Tendered Ballot Paper Issued"]
        """

    def _process_tender_vote(self) -> str:
        return """
        graph TD
            A["Someone Has Already Voted in Your Name"] --> B["Report to Presiding Officer Immediately"]
            B --> C["State Your Identity and Present ID"]
            C --> D["Presiding Officer Issues Tender Ballot Paper"]
            D --> E["Cast Tender Vote on Separate Ballot"]
            E --> F["Vote Sealed Separately for Dispute Resolution"]
            F --> G["File Complaint at Returning Officer's Office"]
        """

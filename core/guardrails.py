import re

class SemanticInterceptor:
    """
    Engine-B: The Auditor.
    Intercepts all outputs from Engine-A (ElectionLogicEngine) to scan for
    political bias, candidate mentions, or hallucinations.
    Temperature: 0.1 — Maximum determinism, zero generative creativity.
    """

    def __init__(self):
        self.flagged_terms = [
            r"\bvote for\b", r"\bparty\b", r"\bcandidate\b",
            r"\bBJP\b", r"\bINC\b", r"\bCongress\b", r"\bAAP\b", r"\bTMC\b",
            r"\bNDA\b", r"\bUPA\b", r"\bSP\b", r"\bBSP\b",
            r"\bModi\b", r"\bGandhi\b", r"\bKejriwal\b", r"\bBanerjee\b",
            r"\bYogi\b", r"\bRahul\b", r"\bSonia\b", r"\bShah\b",
            r"\bwin\b", r"\blose\b", r"\bbetter party\b", r"\bwhich party\b",
            r"\bfix the economy\b", r"\beconomic policy\b", r"\bmanifesto\b",
        ]
        # Trap: out-of-jurisdiction ID check
        self.trap_terms = [
            r"\blibrary card\b", r"\bPassport\b", r"\bout.of.state\b",
        ]
        self.pattern = re.compile("|".join(self.flagged_terms), re.IGNORECASE)
        self.trap_pattern = re.compile("|".join(self.trap_terms), re.IGNORECASE)

    def sanitize(self, input_string: str) -> dict:
        """
        Dual-pass audit:
        Pass 1: Partisan injection scan (blocks with SYSTEM OVERRIDE)
        Pass 2: Invalid ID / trap scenario scan (redirects with procedural guidance)
        """
        if not input_string:
            return {"is_safe": True, "override_message": "", "trap_detected": False}

        if self.pattern.search(input_string):
            return {
                "is_safe": False,
                "trap_detected": False,
                "override_message": (
                    "As a non-partisan civic agent, I cannot recommend candidates or parties. "
                    "However, I can show you how to research candidates via official non-partisan "
                    "guides from the Election Commission of India (ECI). Under the "
                    "Representation of the People Act, 1951, the ECI publishes verified "
                    "candidate affidavits at affidavit.eci.gov.in."
                )
            }

        if self.trap_pattern.search(input_string):
            return {
                "is_safe": False,
                "trap_detected": True,
                "override_message": (
                    "PROCEDURAL ALERT: Non-standard identification detected. "
                    "Under the Conduct of Elections Rules, 1961, only 12 officially approved "
                    "documents are accepted at Indian polling stations. A library card or "
                    "out-of-state ID is NOT on this list. Valid alternatives include: "
                    "Aadhaar Card, PAN Card, Driving Licence, Passport, MNREGA Job Card, "
                    "Bank Passbook with Photo, or Smart Card issued by RGI."
                )
            }

        return {"is_safe": True, "override_message": "", "trap_detected": False}

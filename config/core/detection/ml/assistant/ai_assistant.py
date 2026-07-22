# assistant/ai_assistant.py

class AISecurityAssistant:

    def explain_threat(
            self,
            threat_name,
            score
    ):

        if score > 80:

            severity = "Critical"

        elif score > 60:

            severity = "High"

        elif score > 40:

            severity = "Medium"

        else:

            severity = "Low"

        return f"""
Threat: {threat_name}

Severity: {severity}

Threat Score: {score}

Recommendation:
Investigate the source IP.
Review traffic patterns.
Consider blocking malicious hosts.
"""
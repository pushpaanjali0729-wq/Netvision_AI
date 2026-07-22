BLACKLISTED_IPS = {

    "1.2.3.4",

    "5.6.7.8"
}


class BlacklistDetector:

    def analyze(self, src_ip):

        if src_ip in BLACKLISTED_IPS:

            return {

                "threat": "Blacklisted IP",

                "score": 95
            }

        return None
from tabulate import tabulate

def get_threat_summary():
    threats = [
        {
            "Threat Vector": "Brute Force",
            "Target": "AES Key / Password",
            "Mitigation": "256-bit AES + PBKDF2/bcrypt with salt and iterations"
        },
        {
            "Threat Vector": "Key Interception",
            "Target": "AES Key in Transit",
            "Mitigation": "ECIES Hybrid Encryption, ECDH Key Exchange"
        },
        {
            "Threat Vector": "Quantum Attacks",
            "Target": "RSA Encryption",
            "Mitigation": "Simulated PQ Hybrid Encryption (Kyber/Dilithium)"
        },
        {
            "Threat Vector": "File Tampering",
            "Target": "Stored Files",
            "Mitigation": "SHA-256 Integrity Verification + Tamper Detection"
        },
        {
            "Threat Vector": "Unauthorized Access",
            "Target": "Files/Keys",
            "Mitigation": "Challenge-Response Auth + Session Persistence"
        },
        {
            "Threat Vector": "Forensic Recovery",
            "Target": "Deleted Sensitive Files",
            "Mitigation": "Multi-pass File Shredder (DoD standard)"
        },
        {
            "Threat Vector": "Audit Manipulation",
            "Target": "Logs/History",
            "Mitigation": "Immutable JSON Logs + Optional Blockchain Anchoring"
        },
        {
            "Threat Vector": "Cloud Leakage",
            "Target": "GDrive Files",
            "Mitigation": "On-device Encryption + Manual Upload/Download"
        }
    ]
    return tabulate(threats, headers="keys", tablefmt="grid")

if __name__ == "__main__":
    print(get_threat_summary())

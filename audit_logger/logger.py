import json
from datetime import datetime
import os

LOG_FILE = "/content/FortiCryptX-Colab/audit_logger/logs.json"

def log_event(event_type, details):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "event_type": event_type,
        "details": details
    }
    with open(LOG_FILE, "a") as f:
        json.dump(entry, f)
        f.write("\n")

def read_logs():
    if not os.path.exists(LOG_FILE):
        return []
    logs = []
    with open(LOG_FILE, "r") as f:
        for line in f:
            try:
                logs.append(json.loads(line.strip()))
            except json.JSONDecodeError:
                continue
    return logs

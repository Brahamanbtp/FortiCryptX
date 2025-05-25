import markdown
import json
from datetime import datetime
from fpdf import FPDF

LOG_FILE = "/content/FortiCryptX-Colab/audit_logger/logs.json"

def generate_markdown_report(output_path="/content/audit_report.md"):
    with open(LOG_FILE) as f:
        logs = [json.loads(line) for line in f.readlines()]

    md_lines = ["# 🔍 FortiCryptX Audit Report", f"**Generated:** {datetime.utcnow().isoformat()}", "---"]
    for log in logs:
        md_lines.append(f"### 🕒 {log['timestamp']}")
        md_lines.append(f"**Type:** {log['event_type']}")
        md_lines.append(f"**Details:** `{log['details']}`")
        md_lines.append("---")

    with open(output_path, "w") as f:
        f.write("\n".join(md_lines))

def generate_pdf_report(md_path="/content/audit_report.md", pdf_path="/content/audit_report.pdf"):
    with open(md_path, "r") as f:
        lines = f.readlines()

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in lines:
        clean_line = line.strip().replace("**", "").replace("#", "").replace("`", "")
        if clean_line:
            pdf.multi_cell(0, 10, clean_line)

    pdf.output(pdf_path)

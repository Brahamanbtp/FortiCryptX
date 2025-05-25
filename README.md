# 🔐 FortiCryptX-Colab

**Secure, Intelligent & Modular File Encryption with Post-Quantum Simulation and Cloud Integration**

FortiCryptX is an advanced hybrid cryptographic framework built for Google Colab environments. It combines AES + RSA encryption, post-quantum simulation, ML-based anomaly detection, blockchain audit logging, and Google Drive integration—all in a user-friendly modular design.

---

## 🚀 Features

- 🔒 **Hybrid Encryption** – AES for data + RSA for key wrapping
- 🧬 **Post-Quantum Simulation** – Kyber/Dilithium-based key exchange (simulated)
- 🔁 **Key Management** – Generation, rotation, audit, expiry prediction (ML)
- 🛡️ **Tamper Detection** – SHA-256 hashing with integrity checks
- 🧨 **Secure File Shredding** – Multi-pass overwrite before delete
- 📁 **Google Drive Sync** – Upload/download & persistent storage
- 📊 **Entropy & Anomaly Detection** – ML for suspicious file detection
- 📜 **Auditing** – JSON logs, PDF/Markdown reports, optional blockchain hashes
- 👥 **Simulated Multi-User** – Roles (Admin/Viewer), challenge-response auth
- 🌐 **Colab-Friendly** – UI via ipywidgets or Gradio

---

## 🧠 System Architecture

- **Encryption**: AES-GCM (Symmetric) + RSA (Asymmetric)
- **PQ Simulation**: Hybrid mode with simulated Kyber + RSA
- **Logging**: Action logs with blockchain anchoring (optional)
- **Audit Tools**: Report generation + session visualization

---

## 📁 Project Structure

| Directory | Description |
|----------|-------------|
| `crypto_engine/` | AES, RSA, ECIES, PBE, signatures, entropy tools |
| `key_management/` | Key generation, rotation, audit, ML expiry prediction |
| `security_tools/` | Hash verification, tamper check, secure deletion |
| `cloud_integration/` | Google Drive picker & persistence layer |
| `ui/` | Gradio/ipywidgets-based interactive UI components |
| `audit_logger/` | JSON logging, report generation, blockchain anchor |
| `pq_simulation/` | Kyber/Dilithium key exchange simulation |
| `benchmarking/` | Performance evaluation, threat model tables |
| `main.ipynb` | Main notebook for execution in Google Colab |
| `requirements.txt` | Dependencies list |

---

## 📈 Performance Metrics

| Feature | Performance |
|---------|------------|
| AES-RSA Encryption | 20–40 ms |
| Entropy Check | < 10 ms |
| Key Rotation | Dynamic/Timed |
| PQ Simulation | ~100 ms overhead |
| File Upload/Drive Sync | Instant via widgets |
| Log Export (PDF/CSV) | < 500 ms |

---

## 🔐 Security Highlights

- Hybrid crypto (AES-GCM + RSA-2048)
- Simulated PQ-safe encryption
- SHA-256 hashing and integrity check
- Ephemeral key sessions for secrecy
- Challenge-response before decryption
- Blockchain-compatible action logs
- Secure overwrite-based file shredding

---

## 🧩 Applications

- 🏥 Healthcare: EMR encryption with audit logs
- 🏛️ Government: Tamper-resistant file storage
- ☁️ Cloud & Education: Lightweight Colab-based encryption
- 🛠️ Research: PQ crypto benchmarking & anomaly testing
- 📈 Finance: Logable secure transaction payloads

---

## 💡 Future Work

- 🧠 AI-Powered Smart Key Rotation
- 🔐 Full PQC Implementation (Kyber/Dilithium Libraries)
- ⛓️ Blockchain audit trail support with Ethereum/Polygon
- 🕸️ Federated key exchange between users
- 👥 RBAC (Role-Based Access Control)
- 🔒 TPM/HSM Hardware support in browser/Colab

---

## 🛠 Requirements

- Python 3.7+
- Colab/Jupyter (recommended)
- `cryptography`, `pycryptodome`, `ipywidgets`, `matplotlib`, `reportlab`, `gradio`

```bash
pip install -r requirements.txt
```

---

## 📸 UI Preview

![UI Preview](Workflow_Diagram.jpg)

---

**Made with 🔐 by Pranay Sharma**  
📧 pranay.sharma2022@vitstudent.ac.in

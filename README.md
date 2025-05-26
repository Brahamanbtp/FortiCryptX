![Workflow_Diagram](https://github.com/user-attachments/assets/f9e60115-68d0-46a5-b349-e4ef521cc34a)

# 🔐 FortiCryptX-Colab

**Secure, Intelligent & Modular File Encryption with Post-Quantum Simulation and Cloud Integration**

FortiCryptX is an advanced hybrid cryptographic framework built for Google Colab environments. It integrates AES + RSA encryption, post-quantum simulation, ML-based anomaly detection, blockchain audit logging, and Google Drive support—all wrapped in a modular, user-friendly design.

---

## 🚀 Features

- 🔒 **Hybrid Encryption** – AES for data, RSA for key wrapping  
- 🧬 **Post-Quantum Simulation** – Simulated Kyber/Dilithium-based key exchange  
- 🔁 **Key Management** – Generation, rotation, ML-based expiry prediction  
- 🛡️ **Tamper Detection** – SHA-256 hashing and integrity verification  
- 🧨 **Secure File Shredding** – Multi-pass data overwrite before deletion  
- 📁 **Google Drive Sync** – File I/O with persistent cloud storage  
- 📊 **Entropy & Anomaly Detection** – ML for detecting suspicious patterns  
- 📜 **Auditing** – JSON logs, PDF/Markdown reports, optional blockchain anchoring  
- 👥 **Simulated Multi-User** – Admin/Viewer roles, challenge-response login  
- 🌐 **Colab-Friendly** – Interactive UI via `ipywidgets` or `Gradio`  

---

## 🧠 System Architecture

- **Encryption Stack**: AES-GCM (Symmetric) + RSA-2048 (Asymmetric)  
- **PQ Simulation**: Hybrid with simulated Kyber + RSA fallback  
- **Logging**: JSON action logs, blockchain-compatible hashes  
- **Audit Tools**: Auto-generated reports, visualization features  

---

## 📁 Project Structure

| Directory             | Description |
|----------------------|-------------|
| `crypto_engine/`     | Core encryption modules: AES, RSA, ECIES, PBE, entropy tools |
| `key_management/`    | Key generation, ML-based rotation, auditing |
| `security_tools/`    | Integrity check, tamper detection, secure deletion |
| `cloud_integration/` | Google Drive picker & persistent file sync |
| `ui/`                | `Gradio` / `ipywidgets` interface components |
| `audit_logger/`      | Logging, reporting, optional blockchain anchoring |
| `pq_simulation/`     | Kyber/Dilithium key exchange simulation layer |
| `benchmarking/`      | Performance metrics, threat models |
| `main.ipynb`         | Entry point notebook for Google Colab |
| `requirements.txt`   | Python dependency list |

---

## 📈 Performance Metrics

| Feature                  | Performance         |
|--------------------------|---------------------|
| AES-RSA Encryption       | 20–40 ms            |
| Entropy Check            | < 10 ms             |
| Key Rotation             | Timed / On-demand   |
| PQ Simulation Overhead   | ~100 ms             |
| File Upload/Drive Sync   | Instant (via UI)    |
| Log Export (PDF/CSV)     | < 500 ms            |

---

## 🔐 Security Highlights

- Hybrid encryption (AES-GCM + RSA-2048)  
- Simulated post-quantum cryptography  
- Secure hashing (SHA-256) and tamper detection  
- Ephemeral key sessions and challenge-based access  
- Blockchain-compatible logs  
- Multi-pass secure file shredding  

---

## 🧩 Applications

- 🏥 **Healthcare** – Encrypt EMRs with audit capability  
- 🏛️ **Government** – Tamper-proof secure storage  
- ☁️ **Cloud & Education** – Lightweight Colab-based encryption  
- 🛠️ **Research** – PQ crypto benchmarking, anomaly modeling  
- 📈 **Finance** – Secure, loggable transaction payloads  

---

## 💡 Future Work

- 🧠 AI-powered smart key rotation  
- 🔐 Full PQC implementation (Kyber/Dilithium libraries)  
- ⛓️ Blockchain audit trail with Ethereum/Polygon  
- 🕸️ Federated key exchange & group encryption  
- 👥 RBAC (Role-Based Access Control)  
- 🔒 TPM/HSM support in-browser and in Colab  

---

## 🛠 Requirements

- Python 3.7+  
- Google Colab or Jupyter Notebook  
- Dependencies:  
  `cryptography`, `pycryptodome`, `ipywidgets`, `matplotlib`, `reportlab`, `gradio`

```bash
pip install -r requirements.txt
```

📄 License
This project is governed by a restricted academic license.
See LICENSE.md for complete terms and usage restrictions.

Made with 🔐 by Pranay Sharma
📧 pranay.sharma2022@vitstudent.ac.in

# AI-Based Fake Identity & Document Screening System (RakshaScan / SentinelBorder)

An AI-powered border checkpoint screening platform designed for automated document analysis, digital forgery detection, ICAO Doc 9303 compliance validation, 1-to-1 facial biometric verification, and explainable border risk assessment.

---

## 🎯 Key Capabilities

1. **Module 1: OCR & MRZ Field Extraction**
   - High-precision extraction of VIZ (Visual Inspection Zone) and MRZ (Machine Readable Zone: TD1, TD2, TD3).
   - Per-field confidence scores for auditability.
2. **Module 2: Document Rule & Logic Validator**
   - ICAO Doc 9303 weighted check-digit computation (`[7, 3, 1]`).
   - Cross-parity comparison between VIZ and MRZ to catch selective alterations.
   - Watchlist & Interpol SLTD cross-referencing.
3. **Module 3: Tampering & Digital Forensics (Core AI Innovation)**
   - **Error Level Analysis (ELA)** for detecting JPEG compression inconsistencies.
   - **Local Noise Analysis** to detect spliced and pasted photo elements.
   - **Copy-Move & Cloning Detection** using SIFT feature clustering.
   - **EXIF & Metadata Forensic Scrubber** to catch image manipulation tools (Photoshop, GIMP, Canva).
   - **Visual Heatmap Generation** showing precise suspicious bounding boxes.
4. **Module 4: Face Verification & Anti-Spoofing**
   - 1-to-1 facial feature matching using ArcFace (InsightFace) deep cosine embeddings.
   - Anti-spoofing and liveness detection (blink detection and texture analysis).
5. **Explainable Multi-Pillar Risk Engine**
   - Transparent $0 - 100$ scoring formula mapping to Green (Clear), Amber (Secondary Review), and Red (Detain).
6. **Cryptographic SHA-256 Hash Chain**
   - Append-only, tamper-evident audit ledger admissible in legal and forensic investigations.

---

## 📁 Repository Structure

```text
fake_Identity_ai/
├── PROJECT_BLUEPRINT.md          # Complete Architecture & Hackathon Proposal
├── backend/                      # Python FastAPI Screening Engine
│   ├── app/
│   │   ├── api/v1/endpoints/     # REST Endpoints (screen, ocr, validate, forensics, biometrics, audit)
│   │   ├── core/                 # App configuration & security settings
│   │   ├── modules/              # Core AI & Forensic Engines
│   │   │   ├── ocr_engine.py
│   │   │   ├── rules_validator.py
│   │   │   ├── tampering_detector.py
│   │   │   ├── face_verifier.py
│   │   │   └── risk_scorer.py
│   │   ├── database/             # SQLite/PostgreSQL schema & Audit Ledger
│   │   └── main.py
│   └── requirements.txt
├── frontend/                     # Checkpoint Officer Terminal (React + TypeScript + Tailwind)
│   ├── src/
│   │   ├── components/           # Scanner, Heatmap viewer, Biometric matcher, Risk gauge
│   │   ├── pages/                # Officer Dashboard, Investigation Portal, Audit Viewer
│   │   └── App.tsx
│   └── package.json
└── samples/                      # Synthetic test documents (Genuine, Tampered Photo, Tampered MRZ)
```

---

## 🚀 Quick Start Guide

### Prerequisites

- Python 3.10+ (Current system: Python 3.13)
- Node.js 18+ (Current system: Node v24)
- Webcam (for live face verification)

### Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

- API Documentation available at: `http://localhost:8000/docs`

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

- Officer Terminal available at: `http://localhost:5173`

---

## ⚖ Standards & Compliance

- **ICAO Doc 9303**: Machine Readable Travel Documents specification.
- **ISO/IEC 19794-5**: Biometric data interchange formats (Face image data).
- **NIST AI RMF**: Transparent, explainable, and fair risk governance.
- **Digital Personal Data Protection Act (DPDP Act 2023)**: Ephemeral biometric processing, zero raw biometric persistence in audit logs.

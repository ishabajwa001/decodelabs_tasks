# 🧠 DecodeLabs Tasks — Isha Javed

A collection of 4 Python projects completed as part of the DecodeLabs internship, covering AI, Machine Learning, NLP, and Computer Vision.

---

## 📁 Repository Structure

```
decodelabs_tasks/
├── Task-1-Isha_Javed/     # RuleWise — Rule-Based AI Chatbot
├── Task-2-Isha_Javed/     # Iris Flower Classification
├── Task-3-Isha_Javed/     # Career Compass — AI Career Recommender
└── Task-4-Isha_Javed/     # Image & Text Recognition Pipeline
```

---

## 🗂️ Tasks Overview

### Task 1 — RuleWise: Rule-Based AI Chatbot
> **`Task-1-Isha_Javed/`** &nbsp;|&nbsp; Python &nbsp;|&nbsp; No external libraries

A rule-based chatbot built in pure Python that teaches users how rule-based systems work by being a live, working example of one. Every response comes with an explanation of how and why the bot responded that way.

**Key Features:**
- 6-step input processing pipeline (input → sanitize → match → respond)
- Dictionary-based knowledge base covering AI, ML, chatbots, and technical concepts
- Personalized exit summary with a learning recap
- Zero dependencies — runs with `python RuleWise.py`

---

### Task 2 — Iris Flower Classification
> **`Task-2-Isha_Javed/`** &nbsp;|&nbsp; Python &nbsp;|&nbsp; scikit-learn, pandas, matplotlib, seaborn

A supervised machine learning project that classifies Iris flowers into 3 species using the K-Nearest Neighbors (KNN) algorithm, with full algorithm comparison, cross-validation, and custom prediction support.

**Key Features:**
- KNN, Decision Tree, and Logistic Regression compared head-to-head
- Elbow Method to find optimal K value
- 5-Fold Cross-Validation for consistency checks
- 12-panel visualisation dashboard
- Best accuracy: **96.67%** (KNN, K=1)

| Algorithm | Accuracy | F1 Score |
|-----------|----------|----------|
| ✅ KNN (K=1) | 96.67% | 0.9666 |
| Decision Tree | 93.33% | 0.9333 |
| Logistic Regression | 93.33% | 0.9333 |

---

### Task 3 — Career Compass: AI Career Recommender
> **`Task-3-Isha_Javed/`** &nbsp;|&nbsp; Python &nbsp;|&nbsp; Standard library only &nbsp;|&nbsp; HTML/CSS/JS

An AI-powered career recommendation engine that matches your skills to the most relevant job roles using TF-IDF vectorization and Cosine Similarity, served through a clean web UI.

**Key Features:**
- Content-based filtering across 20 real job roles
- TF-IDF + Cosine Similarity ranking (industry-standard NLP)
- No database, no login — runs entirely from a CSV file
- Fully deployable on Render, Railway, or PythonAnywhere
- Run with `python app.py` → opens at `http://localhost:5000`

---

### Task 4 — Image & Text Recognition Pipeline
> **`Task-4-Isha_Javed/`** &nbsp;|&nbsp; Python &nbsp;|&nbsp; pytesseract, OpenCV, Pillow, NumPy

A two-path image and text recognition pipeline with pre-processing, confidence filtering, and annotated visual output. Only results with a confidence score ≥ 80% are accepted.

**Key Features:**
- **Path 1 — OCR:** Tesseract (CNN + LSTM) with grayscale, blur, Otsu thresholding, and deskewing
- **Path 2 — Object Detection:** OpenCV Haar Cascade classifiers with bounding boxes
- Supports faces, eyes, upper body, full body, and smile detection
- PSM mode selection for different document types

---

## 🛠️ Tech Stack

| Task | Language | Libraries / Tools |
|------|----------|-------------------|
| Task 1 | Python | Standard library only |
| Task 2 | Python | scikit-learn, pandas, numpy, matplotlib, seaborn |
| Task 3 | Python + HTML/CSS/JS | Standard library, TF-IDF, Cosine Similarity |
| Task 4 | Python | pytesseract, opencv-python, Pillow, NumPy |

---

## ▶️ Quick Start

Each task is self-contained. Navigate into the folder and follow its own README.

```bash
# Task 1
cd Task-1-Isha_Javed
python RuleWise.py

# Task 2
cd Task-2-Isha_Javed
pip install scikit-learn pandas matplotlib seaborn numpy
python iris_classification.py

# Task 3
cd Task-3-Isha_Javed/career_compass
python app.py

# Task 4
cd Task-4-Isha_Javed
pip install pytesseract opencv-python pillow numpy
python recognition.py --path 1 --image sample_images/sample_text_simple.png
```

---

> Built by **Isha Javed**
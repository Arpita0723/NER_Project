# Named Entity Recognition (NER) System for Low-Resource Languages

## Overview

This project focuses on building a Named Entity Recognition (NER) system for low-resource languages using transformer-based models and Django integration.

Named Entity Recognition is an important Natural Language Processing (NLP) task used to identify entities such as persons, locations, and organizations from raw text.

The project combines machine learning, deep learning, APIs, and backend development to create a real-time multilingual entity recognition system.

---

# Problem Statement

Building NLP systems for low-resource languages is challenging because:

- Annotated datasets are limited
- Datasets contain noisy labels
- Model generalization becomes difficult
- Training high-quality multilingual models requires large computational resources

This project aims to explore these challenges and develop a practical NER system using transformer-based approaches.

---

# Objectives

The main objectives of this project are:

- Build a multilingual NER system
- Perform experiments on low-resource language datasets
- Fine-tune transformer-based models
- Evaluate model performance
- Integrate the model into a Django-based NLP application
- Provide real-time entity prediction through APIs

---

# Technologies Used

- Python
- Django
- HuggingFace Transformers
- PyTorch
- Django REST Framework
- WikiAnn Dataset
- HTML/CSS
- Google Colab

---

# Dataset

The project uses the multilingual WikiAnn dataset.

The dataset contains entity annotations for multiple languages such as:

- Assamese
- Hindi
- Bengali
- Tamil
- Telugu
- Kannada
- Malayalam
- Marathi
- Punjabi
- Gujarati
- Odia

Entity tags include:

- PER → Person
- LOC → Location
- ORG → Organization

---

# Model and Training

Initially, fine-tuning experiments were performed using IndicBERT on multilingual WikiAnn datasets.

The training pipeline included:

1. Dataset loading
2. Tokenization
3. Label alignment
4. Transformer fine-tuning
5. Evaluation using Precision, Recall, and F1-score

Due to noisy annotations and limited dataset quality, pretrained transformer models were later used to achieve better prediction accuracy.

---

# Tokenization and Label Alignment

Transformer models split words into sub-tokens. Therefore, labels must be aligned correctly with tokens during preprocessing.

Special tokens and padding tokens were ignored during training using:

```python
-100
```

This prevents unnecessary loss calculation for padding and subword tokens.

---

# Fine-Tuning Process

The fine-tuning process involved:

1. Loading multilingual datasets from WikiAnn
2. Tokenizing sentences using transformer tokenizer
3. Aligning labels with generated tokens
4. Training the transformer model using HuggingFace Trainer API
5. Evaluating the model using NLP metrics

Fine-tuning helped adapt the pretrained transformer model specifically for the Named Entity Recognition task.

---

# Evaluation Metrics

The model performance was evaluated using the following metrics:

## Precision

Precision measures how many predicted entities are actually correct.

## Recall

Recall measures how many actual entities were correctly identified by the model.

## F1-Score

F1-score balances both precision and recall.

The `seqeval` metric library was used for computing evaluation metrics.

---

# Django Integration

The trained/pretrained transformer model was integrated into a Django backend using Django REST Framework.

The Django API:

- receives user text input
- sends text to the transformer model
- processes predictions
- returns detected entities as JSON response

This allows real-time Named Entity Recognition directly through the web application.

---

# System Workflow

```text
User Input
     ↓
Django REST API
     ↓
Tokenizer
     ↓
Transformer NER Model
     ↓
Predicted Entities
     ↓
Output Display
```

---

# Input and Output Example

## Input

```text
Narendra Modi visited Mumbai.
```

## Output

```text
Narendra Modi → PER
Mumbai → LOC
```

---

# Features

- Real-time entity recognition
- Transformer-based NLP pipeline
- Django REST API integration
- Multilingual support
- Web interface for testing predictions
- Support for low-resource languages

---

# Project Structure

```text
NER_Project/

├── ner_app/
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   ├── templates/

├── ner_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py

├── manage.py
├── requirements.txt
└── README.md
```

---

# How to Run the Project

## Step 1: Clone Repository

```bash
git clone https://github.com/Arpita0723/NER_Project.git
```

## Step 2: Move to Project Directory

```bash
cd NER_Project
```

## Step 3: Create Virtual Environment

```bash
python -m venv venv
```

## Step 4: Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

## Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 6: Run Django Server

```bash
python manage.py runserver
```

## Step 7: Open in Browser

```text
http://127.0.0.1:8000/
```

---

# API Endpoint

## POST Request

```text
/predict/
```

## Example Request

```json
{
  "text": "Narendra Modi visited Mumbai"
}
```

## Example Response

```json
[
  {
    "word": "Narendra Modi",
    "entity": "PER"
  },
  {
    "word": "Mumbai",
    "entity": "LOC"
  }
]
```

---

# Limitations

- Dataset contains noisy annotations
- Fine-tuned model accuracy is limited
- Large transformer models require higher memory
- Deployment optimization is still limited
- Some multilingual predictions may be inconsistent

---

# Future Improvements

- Improve multilingual support
- Use cleaner datasets
- Deploy on cloud platforms
- Improve frontend interface
- Increase model accuracy
- Train custom lightweight transformer models
- Add support for more entity categories

---

# Conclusion

This project successfully demonstrates the integration of transformer-based NLP models with Django for multilingual Named Entity Recognition.

The project highlights the challenges of working with low-resource languages and provides a practical end-to-end NLP application capable of real-time entity prediction.

The system combines:

- Machine Learning
- Deep Learning
- NLP
- APIs
- Backend Development

into one complete application.

---

# Author

**Arpita Singh**

Department of Computer Science  
Indian Institute of Technology (BHU), Varanasi

Under the guidance of  
**Prof. Anil Kumar Singh**

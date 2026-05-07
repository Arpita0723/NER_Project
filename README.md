# Named Entity Recognition (NER) System for Low-Resource Languages

## Overview
This project is a transformer-based Named Entity Recognition (NER) system developed for low-resource languages. The system identifies entities such as Persons, Locations, and Organizations from user input text.

The project combines Natural Language Processing (NLP), HuggingFace Transformers, and Django to create a real-time prediction system.

---

## Features
- Multilingual NER support
- Transformer-based NLP model
- Real-time entity prediction
- Django backend integration
- REST API support
- Web interface for testing predictions

---

## Technologies Used
- Python
- Django
- HuggingFace Transformers
- PyTorch
- WikiAnn Dataset
- HTML/CSS
- REST Framework

---

## Dataset
The project uses the WikiAnn multilingual dataset for training and evaluation.

The dataset contains labeled entities such as:
- PER (Person)
- LOC (Location)
- ORG (Organization)

---

## Model
The system uses a pretrained transformer model for token classification.

Main steps:
1. Tokenization
2. Label alignment
3. Fine-tuning
4. Evaluation using Precision, Recall, and F1-score

---

## System Workflow
User Input → Django API → Transformer Model → Predicted Entities

---

## Example

### Input
```text
Narendra Modi visited Mumbai.

### Output
Narendra Modi → PER
Mumbai → LOC

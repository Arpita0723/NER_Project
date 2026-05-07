from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")
tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")

ner_pipeline = pipeline(
    "ner",
    model=model,
    tokenizer=tokenizer,
    aggregation_strategy="simple",
    ignore_labels=[]  
)

def merge_tokens(entities):
    merged = []
    current_word = ""
    current_label = ""

    for ent in entities:
        word = ent['word']
        label = ent.get('entity_group', ent.get('entity', 'O'))

        if word.startswith("##"):
            current_word += word[2:]
        else:
            if current_word:
                merged.append({"word": current_word, "entity": current_label})
            current_word = word
            current_label = label

    if current_word:
        merged.append({"word": current_word, "entity": current_label})

    return merged

def home(request):
    return render(request, 'index.html')
@api_view(['POST'])
def predict_ner(request):
    text = request.data.get("text")

    if not text:
        return Response({"error": "No text provided"})

    raw = ner_pipeline(text)
    print("RAW OUTPUT:", raw)

    return Response(raw)   # 🔥 bypass merge for now
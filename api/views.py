from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import RoastSession
from .serializers import RoastSessionSerializer
from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer
import torch

# ==========================================
# LOAD AI MODELS INTO MEMORY ONCE
# ==========================================
print("Loading AI Models... (This takes a moment on first run)")

# 1. The Sentiment Classifier
# Note: If you pushed your custom model to HuggingFace, replace the string below with "your-username/cinematic-roaster-sentiment"
classifier = pipeline("sentiment-analysis")
# 2. The Roaster (Flan-T5)
roaster_tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
roaster_model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")

print("AI Models loaded successfully!")

# ==========================================
# API VIEWS
# ==========================================

@api_view(['POST'])
def analyze_and_roast(request):
    # 1. Get the review text from the frontend
    review_text = request.data.get('review', '')
    
    if not review_text:
        return Response({"error": "Please provide a review text."}, status=400)

    # 2. Run Sentiment Analysis
    result = classifier(review_text)[0]
    label = result['label'] # Will be 'POSITIVE' or 'NEGATIVE'
    
    roast_response = ""
    
    # 3. If Negative, trigger the Roaster AI
       # 3. If Negative, trigger the Roaster AI
    if label == 'NEGATIVE':
        prompt = f"""Review: "{review_text}"
        
        Task: Write a 2-sentence funny, sarcastic insult directed at the person who wrote this review because they have bad taste in cinema."""
        
        inputs = roaster_tokenizer(prompt, return_tensors="pt")
        
        # Added repetition_penalty=2.0 to stop word loops
        outputs = roaster_model.generate(**inputs, max_new_tokens=50, repetition_penalty=2.0)
        roast_response = roaster_tokenizer.decode(outputs[0], skip_special_tokens=True)
    else:
        roast_response = None

    # 4. Save to Database
    session = RoastSession.objects.create(
        review_text=review_text,
        detected_sentiment=label,
        roast_response=roast_response
    )
    
    # 5. Return JSON
    serializer = RoastSessionSerializer(session)
    return Response(serializer.data, status=201)
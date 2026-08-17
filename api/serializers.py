from rest_framework import serializers
from .models import RoastSession

class RoastSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoastSession
        fields = ['id', 'review_text', 'detected_sentiment', 'roast_response', 'created_at']
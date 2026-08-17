from django.db import models

class RoastSession(models.Model):
    # The text the user typed in
    review_text = models.TextField()
    
    # What our DistilBERT model guessed (Positive/Negative)
    detected_sentiment = models.CharField(max_length=20)
    
    # The generated roast from Flan-T5 (can be blank if it was a positive review)
    roast_response = models.TextField(blank=True, null=True)
    
    # Automatically record the time it happened
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.detected_sentiment} - {self.review_text[:50]}..."
from django import forms
from .models import Review

# Form for a review
class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField(required=True, max_value=5, help_text="Enter a star rating from 1-5")
    comments = forms.CharField(required=False, max_length=500, help_text="Enter any comments")

    class Meta:
        model = Review
        fields = ('user', 'property', 'rating', 'comments')
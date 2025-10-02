from django import forms
from .models import Ad

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'description', 'price', 'category', 'condition', 'location', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

from django import forms

from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'
        widgets = {
            'content':forms.Textarea(attrs={'placeholder':'Write your Post here'})
        }
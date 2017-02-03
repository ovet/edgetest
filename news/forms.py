from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 20}))

    class Meta:
        model = Article
        fields = ('title', 'body', 'publish')

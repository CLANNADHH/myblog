from django import forms
from article.models import ArticlePost


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = ArticlePost
        fields = ("author", "title", 'body')

from django import forms
from . import models


class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title','body','slug','thumb']



class CreateComment(forms.Form):
    comment = forms.CharField(label="",widget=forms.Textarea(attrs={'rows':'3','class':'form-control'}))

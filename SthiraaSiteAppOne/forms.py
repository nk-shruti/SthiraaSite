
from django.forms import ModelForm
from django import forms
from .models import article

# our new form
class ArticleForm(ModelForm):
    class Meta:
        model = article
        fields = ['heading', 'author','date','photo','content']
        # widgets = {
        #     'heading': forms.TextInput(attrs={'class': 'myfieldclass'}),
        #     'author': forms.TextInput(attrs={'class': 'myfieldclass'})
        # }

        # heading = forms.CharField(required=True)
        # author = forms.CharField(
        #     required=True,
        #     widget=forms.Textarea
        # )

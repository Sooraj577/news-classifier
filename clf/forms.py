from django import forms


class NewsForm(forms.Form):
    news_text = forms.CharField(label='Your name', widget=forms.Textarea)

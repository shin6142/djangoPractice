from django import forms
from .models import Post


class PostInsertForm(forms.ModelForm):

    title = forms.CharField(label='タイトル')
    content = forms.Textarea()
    is_published = forms.BooleanField(label='公開', required=False)
    image = forms.ImageField(label='画像', required=False)

    class Meta:
        model = Post
        fields = '__all__'


class PostUpdateForm(forms.Form):

    title = forms.CharField(label='タイトル')
    content = forms.Textarea()
    is_published = forms.BooleanField(label='公開', required=False)
    image = forms.ImageField(label='画像', required=False)

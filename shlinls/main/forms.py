from django import forms
from .models import Links


class LinkForm(forms.ModelForm):
    link = forms.URLField(
        label='Полная ссылка',
        help_text='Длина полной ссылки не более 250 символов'
    )

    slug = forms.SlugField(
        label='Короткая ссылка',
        help_text='Короткая ссылка не должна повторяться'
    )

    class Meta:
        model = Links
        fields = ['user', 'link', 'slug']
        widgets = {
            'user': forms.HiddenInput(),
        }
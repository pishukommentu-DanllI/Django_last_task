from django import forms
from .models import category, Publishing_house, Text


class One(forms.ModelForm):
    Info = forms.CharField(label='About you', widget=forms.TextInput())

    CATEGORY_CHOICES = [(i.id, i.name) for i in category.objects.all()]
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, label='Катиегории')

    Publishing_house_choice = [(i.id, i.name) for i in Publishing_house.objects.all()]
    publishing_house = forms.MultipleChoiceField(choices=Publishing_house_choice, label='Издательства')

    class Meta:
        model = Text
        exclude = ('Info', 'category', 'publishing_house')
        labels = {
            'title': 'Заголовок',
            'img_href': 'URL or Name_img_in_server:',
            'content': 'Контент:',
            'CheckBox': 'Публикация',
        }


# class One(forms.Form):
#     Title = forms.CharField(label='Заголовок:', widget=forms.TextInput())
#     Url = forms.CharField(label='URL or Name_img_in_server:', widget=forms.TextInput())
#     TextArea = forms.CharField(label='Контент:', widget=forms.Textarea())
#     CheckBox = forms.CharField(label='Публикация', widget=forms.CheckboxInput())
#
#     CATEGORY_CHOICES = [(i.id, i.name) for i in category.objects.all()]
#
#     Selection = forms.ChoiceField(choices=CATEGORY_CHOICES, label='Катиегории')
#
#     Info = forms.CharField(label='About you', widget=forms.TextInput())
#
#     Publishing_house_choice = [(i.id, i.name) for i in Publishing_house.objects.all()]
#     Publishing_house_selection = forms.ChoiceField(choices=Publishing_house_choice, label='Издательства')

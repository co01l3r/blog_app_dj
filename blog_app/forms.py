from django.forms import ModelForm
from .models import Topic
from django import forms


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

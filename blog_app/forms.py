from django.forms import ModelForm
from .models import Topic
from django import forms


class TopicForm(ModelForm):
    """A form for creating or updating a `Topic` object.

    Attributes:
        Meta: A nested class containing additional metadata for the form.
            model (Topic): The model to use for the form.
            fields (str): A string indicating that all fields of the model should be included in the form.
            widgets (dict): A dictionary specifying the widget to use for the `tags` field.
    """
    class Meta:
        model = Topic
        fields = '__all__'
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

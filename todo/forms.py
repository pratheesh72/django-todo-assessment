from django import forms
from django.core.exceptions import ValidationError

from .models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ["title"]

    def clean_title(self):

        title = self.cleaned_data[
            "title"
        ].strip()

        if len(title) < 3:

            raise ValidationError(
                "Task title must contain at least 3 characters."
            )

        return title

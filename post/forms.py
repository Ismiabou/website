from django.forms import ModelForm

from .models import Commentaire


class CommentForm(ModelForm):
    class Meta:
        model = Commentaire
        fields = ['commentaire']

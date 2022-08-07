from django.forms import ModelForm
from App.models import TODO


class TODOForm(ModelForm):
    class Meta:
        model = TODO
        fields = ['title', 'description', 'status','deadline']
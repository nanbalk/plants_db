from django.forms import ModelForm
from .models import Plants

class PlantsForm(ModelForm):
    class Meta:
        model = Plants
        fields = '__all__'

# class PlantsRetreive(ModelForm):
#     class meta:
#         model = Plants
#         fields = ['name', 'bioactive_compound', 'uses']
from django.forms import ModelForm,forms
from .models import Student,Achivements




class AchievementForm(ModelForm):

    class Meta:
        model = Achivements
        fields = '__all__'
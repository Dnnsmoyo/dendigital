from django.forms import ModelForm
from .models import Profile, Document

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['picture','gender','country']
        
class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = ['doc']
        

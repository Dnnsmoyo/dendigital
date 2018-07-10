from rest_framework.serializers import ModelSerializer
from .models import Document, Profile

class DocumentSerializer(ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'
        
class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

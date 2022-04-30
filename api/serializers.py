from dictionary.models import Word
from rest_framework.serializers import ModelSerializer

class WordSerializer(ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'

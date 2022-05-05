from account.models import Collection
from dictionary.models import Word
from rest_framework.serializers import ModelSerializer


class WordSerializer(ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'


class CollectionSerializer(ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'

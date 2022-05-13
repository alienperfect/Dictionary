from apps.account.models import Collection
from apps.dictionary.models import Word
from rest_framework.serializers import ModelSerializer


class WordSerializer(ModelSerializer):
    class Meta:
        model = Word
        exclude = ['word']


class CollectionSerializer(ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'

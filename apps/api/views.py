from apps.account.models import Collection
from apps.api.serializers import WordSerializer, CollectionSerializer
from apps.dictionary.models import Word
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class WordAPIView(APIView):
    def get(self, request, format=None, **kwargs):
        instance = Word.objects.get(word=kwargs.get('word', ''))
        serializer = WordSerializer(instance)
        data = serializer.data

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            parts_of_speech = [field for field in data.keys() if data[field]]
 
            return Response(parts_of_speech)

        return Response(data)


class WordListAPIView(APIView):
    def get(self, request, format=None, **kwargs):
        queryset = Word.objects.filter(word__icontains=kwargs.get('entry', ''))
        data = serializers.serialize('python', queryset, fields=('pk'))

        return Response(data)


class CollectionAPIView(APIView):
    def get(self, request, pk, format=None, **kwargs):
        instance = Collection.objects.get(pk=pk)
        serializer = CollectionSerializer(instance)

        return Response(serializer.data)

    def delete(self, request, pk, format=None, **kwargs):
        instance = Collection.objects.get(pk=pk)
        instance.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

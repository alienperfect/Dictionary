from apps.account.models import Collection
from apps.api.serializers import WordSerializer, CollectionSerializer
from apps.dictionary.models import Word
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class WordAPIView(APIView):
    def get(self, request, format=None, **kwargs):
        word = kwargs.get('word', '')
        instance = Word.objects.get(word=word)
        serializer = WordSerializer(instance)
        data = serializer.data

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            resp = [field for field in data if data[field]]
 
            return Response(resp[2::])

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

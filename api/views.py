import itertools
from api.serializers import WordSerializer
from dictionary.models import Word
from rest_framework.views import APIView
from rest_framework.response import Response


class ApiWord(APIView):
    def get(self, request, format=None, **kwargs):
        word = kwargs.get('word', '')
        instance = Word.objects.get(word=word)
        serializer = WordSerializer(instance)
        data = serializer.data

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            resp = [field for field in data if data[field]]
 
            return Response(resp[2::])

        return Response(data)

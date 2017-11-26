'''
Views
'''

from rest_framework.generics import ListAPIView
from .serializers import CategorySerializer, WordSerializer
from .models import Category, Word

class CategoryList(ListAPIView):
    '''
    Lists all categories.
    '''
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()


class WordList(ListAPIView):
    '''
    Lists all categories.
    '''
    serializer_class = WordSerializer

    def get_queryset(self):
        return Word.objects.all()

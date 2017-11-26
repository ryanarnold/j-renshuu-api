'''
Views
'''

from rest_framework.generics import ListAPIView
from .serializers import CategorySerializer
from .models import Category

class CategoryList(ListAPIView):
    '''
    Lists all categories.
    '''
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()

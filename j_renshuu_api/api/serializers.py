'''
Model Serializers
'''

from rest_framework.serializers import ModelSerializer, StringRelatedField, PrimaryKeyRelatedField
from .models import Category

class CategorySerializer(ModelSerializer):
    '''
    Serializer for Categories.
    '''
    class Meta:
        '''Meta'''
        model = Category
        fields = ('id', 'desc_english', 'desc_japanese')
    
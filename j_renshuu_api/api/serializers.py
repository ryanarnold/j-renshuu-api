'''
Model Serializers
'''

from rest_framework.serializers import ModelSerializer, StringRelatedField, PrimaryKeyRelatedField
from .models import Category, Word

class CategorySerializer(ModelSerializer):
    '''
    Serializer for Categories.
    '''
    class Meta:
        '''Meta'''
        model = Category
        fields = ('id', 'desc_english', 'desc_japanese')


class WordSerializer(ModelSerializer):
    '''
    Serializer for Words.
    '''
    category = CategorySerializer(read_only=True)

    class Meta:
        '''Meta'''
        model = Word
        fields = ('id', 'definition', 'kana', 'kanji', 'category', 'furigana')

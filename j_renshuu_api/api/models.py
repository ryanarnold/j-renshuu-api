'''
Models
'''

from django.db.models import Model, CharField, ForeignKey, CASCADE, DecimalField


class Category(Model):
    '''
    Represents a word's category.
    '''
    desc_english = CharField(max_length=100)
    desc_japanese = CharField(max_length=100)


class Word(Model):
    '''
    Represents a word.
    '''
    definition = CharField(max_length=100)
    kana = CharField(max_length=100)
    kanji = CharField(max_length=100, null=True)
    category = ForeignKey(Category, on_delete=CASCADE)

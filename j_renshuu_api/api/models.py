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

from rest_framework import serializers 
from tutorials.models import Tutorial
 
 
class TutorialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Tutorial
        fields = ('id',
                  'que',
                  'opt1',
                  'opt2',
                  'opt3',
                  'opt4',
                  'que_type',
                  'published')

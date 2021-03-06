from rest_framework import serializers

from .models import Snippet


# ModelSerializers : Snippet 모델의 필드를 그대로 가져다 준다.
# 장고의 폼 클래스와 모델클래스를 제공하듯 비슷한 형태

class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='snippets:snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = (
            'id',
            'title',
            'code',
            'linenos',
            'language',
            'style',

            'owner',
            'highlight',
        )

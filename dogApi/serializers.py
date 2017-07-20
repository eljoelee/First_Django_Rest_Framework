from dogApi.models import Dog
from rest_framework import serializers

# API는 Json, XML 등의 형태로 제공되기 때문에 직렬화(Serialization)를 해야한다.
# DRF의 Serializers는 Django form과 비슷한 형태로 작성한다.

# HyperlinkedModelSerializer : HyperLink Relation
class DogSerializer(serializers.HyperlinkedModelSerializer):

    # Meta : 어떤 model이 쓰여야 하는지 장고에 알려주는 구문(Meta data)
    # 자신이 필요한 정보들을 파악하여 자동으로 Serialize를 수행.
    class Meta:
        model = Dog
        # fields : 포함시킬 데이터 목록
        # HyperlinkedModelSerializer는 HyperLink Relation이기 때문에 pk필드 대신 url필드를 사용한다.
        # 모든 필드(url필드 포함)를 사용하려면  '__all__'를 선언해준다.
        fields = ('dogName', 'dogInfo')
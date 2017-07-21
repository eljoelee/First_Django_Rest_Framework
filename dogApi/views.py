from rest_framework import viewsets
from dogApi.serializers import DogSerializer
from dogApi.models import Dog
from django_filters.rest_framework import DjangoFilterBackend

# 단일 클래스에서 관련있는 view들의 집합을 위해 logic의 결합을 허용하는 것
# ex) 개의 리스트(list)와 세부정보(DetailView)를 장고에서 사용하려면 각각 뷰를 따로 만들어야하지만
# DRF에선 viewSet 하나로 리스트와 세부 정보를 자동 지원한다.

class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

    # filter_backends 변수는 해당 class로 요청이 들어왔을 때 사용할 filter들을 정의할 때 사용
    # DjangoFilterBackend : url에서 fields 이름으로 filter를 사용하고 싶을 때, 사용하는 filter
    # url 뒤에 parameter로 column=값을 설정하여 사용.
    # filter_fields를 통해 column으로 들어올 fields를 설정.
    # 그 외에 들어오는 column에 대해서는 무시.
    # 모든 column : '__all__'
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('dogName',)
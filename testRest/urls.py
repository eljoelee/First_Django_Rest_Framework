from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from dogApi import views

# router : 뷰를 등록하기만 하면 뷰 코드와 뷰, URL이 자동 매핑된다.
router = routers.DefaultRouter()
router.register(r'dogs', views.DogViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    # 탐색 가능한 API의 로그인 뷰와 로그아웃 뷰(인증)에 사용되는 url패턴.
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

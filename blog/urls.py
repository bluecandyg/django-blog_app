# URL 리스트
from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),      # 메인 화면
    # localhost:8000/post/1
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),     # 상세 페이지
    url(r'^post/new/$', views.post_new, name='post_new'),           # 등록 페이지
]
# URL 리스트
from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),      # 메인 화면
    # localhost:8000/post/1
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),     # 상세 페이지
    # url(r'^post/new/$', views.post_new, name='post_new'),                 # 등록 페이지 - model form
    url(r'^post/new/$', views.post_new_form, name='post_new'),              # 등록 페이지 - 기본 form
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),    # 수정 페이지
    url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),   # 삭제 페이지
    url(r'^post/(?P<pk>[0-9]+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),  # 댓글 페이지
    url(r'^comment/(?P<pk>[0-9]+)/approve/$', views.comment_approve, name='comment_approve'),   # 댓글 승인
    url(r'^comment/(?P<pk>[0-9]+)/remove/$', views.comment_remove, name='comment_remove'),      # 댓글 삭제
]
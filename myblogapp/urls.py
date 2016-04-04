from django.conf.urls import url

from myblogapp import views

urlpatterns = [
    url(r'^post/(?P<slug>[^\.]+)/$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^tag/(?P<slug>[^\.]+)/$', views.tag_detail, name='tag_detail'),
    url(r'^post-list/$', views.PostListView.as_view(), name='post-list'),
    url(r'^$', views.IndexView.as_view(), name='index'),
]

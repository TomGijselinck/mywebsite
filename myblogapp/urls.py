from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^post/(?P<slug>[^\.]+)/$', views.PostDetailView.as_view(), name='post_detail'),
	url(r'^$', views.IndexView.as_view(), name='index'),
]

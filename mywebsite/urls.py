from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from mywebsite import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mywebsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('myblogapp.urls', namespace='blog')),
    url(r'^about/', views.AboutView.as_view(), name='about'),
    url(r'^contact/', views.ContactView.as_view(), name='contact'),
    url(r'^$', include('myblogapp.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

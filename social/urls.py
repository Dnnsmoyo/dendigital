"""social URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^chat$',views.IndexView.as_view(),name='index'),
    url(r'^$',views.Index2.as_view(),name='index2'),
    url(r'^upload-doc$',views.DocUploadView.as_view(),name='upload'),
    url(r'^doc/(?P<pk>\d+)$',views.DocDetailView.as_view(),name='doc-detail'),
    url(r'^doclist$',views.DocListView.as_view(),name='doc-list'),
    url(r'^api$',views.DocumentList.as_view(),name='api'),
    url(r'^prof$',views.ProfileList.as_view(),name='prof'),
    url(r'^prof/(?P<pk>\d+)$',views.ProfileDetail.as_view(),name='prof-detail'),
    url(r'^profile_update/(?P<pk>\d+)$',views.ProfileUpdate.as_view(),name='prof-update'),
    url(r'^profile_create$',views.ProfileCreateView.as_view(),name='profile_form'),
    url(r'^profile/(?P<pk>\d+)$',views.ProfileDetailView.as_view(),name='profile-detail'),
    #url(r'^accounts/signup',views.SignUpView.as_view(),name='signup'),
    url(r'^signup',views.SignupView.as_view(),name='signup'),
    url(r'^login',views.LoginView.as_view(),name='login'),
    url(r'^logout',views.LogoutView.as_view(),name='logout'),
    url(r'^api/(?P<pk>\d+)$',views.DocumentDetail.as_view(),name='document-detail'),
    #url('accounts/', include('django.contrib.auth.urls')),
    url('account/', include('allauth.urls')),
    #url(r'^newsletter/', include('newsletter.urls')), 
    url('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf.urls import url
from apps.user import views

urlpatterns = [
    url(r'signup/', views.signup),
    url(r'login/', views.login),
    url(r'$', views.user_list),
    url(r'get/', views.details)
]

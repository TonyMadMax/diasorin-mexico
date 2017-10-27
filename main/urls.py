from django.conf.urls import url
from main import views

# TEMPLATE TAGGING
app_name = 'main'

urlpatterns = [
    url(r'^principal/$',views.principal,name='principal'),
    url(r'^utilidades/$',views.utilidades,name='utilidades'),
    url(r'^otros/$',views.otros,name='otros'),
    url(r'^registrarse/$',views.registrarse,name='registrarse'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]

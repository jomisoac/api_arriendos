from django.conf.urls import url
from clientes import views

urlpatterns = [
    url(r'^clientes/$', views.cliente_list),
    url(r'^clientes/(?P<id>\d+)', views.cliente_detail),
]
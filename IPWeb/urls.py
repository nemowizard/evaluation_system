from django.urls import path

from . import views

app_name = 'IPWeb'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:qualEval_id>/', views.detail, name='detail'),
    path('graph/', views.graph, name='graph'),
]
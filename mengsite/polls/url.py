from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path("mv/<int:pk>", views.myView.as_view(), name='mview'),
    path('mv/new', views.mmodel_new, name='mmodel_form'),
    path('mv/listing', views.MModelListView.as_view(), name='mmodel_listview'),
    path('mv/paginator', views.mmodel_paginator, name='mmodel_paginator'),
    path('experiment', views.experimentalPage, name='experiment'),
]
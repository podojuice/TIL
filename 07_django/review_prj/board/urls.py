from django.urls import path
from . import views



urlpatterns = [
    path('index/', views.index),
    path('greeting/<str:name>/<str:role>/', views.greeting),

    path('articles/new/', views.article_new),
    path('articles/create/', views.article_create),
    path('articles/', views.article_list),
    path('articles/<int:id>/', views.article_detail),
    path('articles/<int:id>/edit/', views.article_edit),
    path('articles/<int:id>/delete/', views.article_delete),
    path('articles/<int:id>/update/', views.article_update),

]
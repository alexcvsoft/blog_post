from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.base, name="main_page"),
    path('create', views.BlogPostCreate.as_view(), name='blogpost_create'),
    path('view', views.BlogPostList.as_view(), name='blogpost_list'),
    path('delete/<str:pk>', views.BlogPostDelete.as_view(), name='blogpost_delete'),
    path('edit/<str:pk>', views.BlogPostUpdate.as_view(), name='blogpost_edit')
]

from django.urls import path
from .views import (
    blog_list_view,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView
)

urlpatterns = [
    path('post/<int:pk>/delete',BlogDeleteView.as_view(),name='post_delete'),
    path('post/<int:pk>/edit', BlogUpdateView.as_view(), name= 'post_edit'),
    path('pos/new', BlogCreateView.as_view(), name='post_new'),
    # BlogListView.as_view() emas, shunchaki blog_list_view yoziladi:
    path('', blog_list_view, name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
]
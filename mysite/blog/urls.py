from django.urls import path
from blog.views import PostsListView, PostDetailView

app_name = 'blog'  # Необязательно, но может быть использовано для namespacing

urlpatterns = [
    path('', PostsListView.as_view(), name='list'),  # по URL http://имя_сайта/blog/ будет выводиться список постов
    path('<int:pk>/', PostDetailView.as_view()),     # по URL http://имя_сайта/blog/число/ будет выводиться пост с определенным номером
]


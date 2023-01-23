from django.urls import path
from .views import render_posts, post_detail

app_name = 'blog'

urlpatterns = [
    path('', render_posts, name='posts'), #cuando visite la página principal '/blog/' se va a renderizar los posts
    path('<int:post_id>', post_detail, name="post_detail")
]
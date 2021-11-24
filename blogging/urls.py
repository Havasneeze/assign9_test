from django.conf.urls import url
from django.urls import path
from blogging.views import stub_view
# from blogging.views import list_view, detail_view
from django.contrib import admin
from blogging.views import PostListView, PostDetailView

# urlpatterns = [
#                 path('', list_view, name="blog_index"),
#                 path('posts/<int:post_id>/', detail_view, name="blog_detail")
#               ]

urlpatterns = [
    path('', PostListView.as_view(), name='blog_index'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='blog_detail')
]


from django.urls import path
from Blog.views import post_detail, post_list, PostListView, post_share

app_name = 'Blog'

urlpatterns = [
    # path('', post_list, name='post_list'),
    path('', PostListView.as_view(), name='post_list'),
    path('<int:post_id>/share/', post_share, name="post_share"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='post_detail'),
    
]
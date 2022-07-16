
from django.urls import path
from .views import (
    BlogView,
    DeleteBlogView,
    OneBlog,
    AddBlog,
    UpdateBlog,
) 

app_name = 'blog'

urlpatterns = [
    path("", BlogView.as_view(), name="BV"),
    path("add/", AddBlog.as_view(), name="AB"),
    path("one/<pk>/", OneBlog.as_view(), name="OB"),
    path("update/<pk>/", UpdateBlog.as_view(), name="UB"),
    path("delete/<pk>/", DeleteBlogView.as_view(), name="DB"),
]

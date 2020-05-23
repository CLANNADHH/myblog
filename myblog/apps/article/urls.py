from django.urls import path, re_path

from . import views
app_name = 'article'

urlpatterns = [
    path('', views.ArticleListView.as_view(), name="article_list"),
    path('article/<int:id>', views.ArticleDetailView.as_view(), name="detail"),
    path('article/create', views.ArticleCreateView.as_view(), name="create"),
    path('article/update/<int:id>', views.ArticleUpdateView.as_view(), name="update"),
    path('article/delete/<int:id>', views.ArticleDeleteView.as_view(), name="delete"),
    re_path('^article/upload_image', views.upload_img, name="upload_img"),
]
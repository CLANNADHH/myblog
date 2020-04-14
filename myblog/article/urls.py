from django.urls import path

from . import views
app_name = 'article'

urlpatterns = [
    path('', views.BlogListView.as_view(), name="article"),
    path('<int:id>',views.BlogView.as_view(), name="detail")
]
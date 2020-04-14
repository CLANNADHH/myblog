from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from article.models import ArticlePost


class BlogListView(ListView):

    template_name = "article/list.html"
    # articles = ArticlePost.objects.all()
    context_object_name = 'articles'
    # 分页
    paginate_by = 1
    model = ArticlePost


class BlogView(DetailView):
    model = ArticlePost
    template_name = "article/detail.html"
    context_object_name = "article"
    pk_url_kwarg = 'id'

    def get_slug_field(self):
        return 'id__id'

# class ArticleView(View):
#     def get(self, request, *args):
#         print(args)
#         articles = ArticlePost.objects.all()
#         print(articles)
#         context = {'articles': articles}
#         return render(request, "article/list.html", context)
#
#     def post(self, request):
#
#         return HttpResponse("POST方法")
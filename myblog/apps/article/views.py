from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from article.models import ArticlePost
import oss2

from myblog import settings


class ArticleListView(ListView):
    """
        文章列表
    """
    template_name = "article/list.html"
    context_object_name = 'articles'
    # 分页
    paginate_by = 10
    page_obj = 1
    model = ArticlePost


class ArticleDetailView(DetailView):
    """
        文章详情页
    """
    model = ArticlePost
    template_name = "article/detail.html"
    context_object_name = "article"
    pk_url_kwarg = 'id'

    def get_object(self, **kwargs):
        obj = super().get_object()
        obj.total_views += 1
        obj.save(update_fields=['total_views'])
        return obj


class ArticleCreateView(LoginRequiredMixin, CreateView):
    # 登录链接
    login_url = reverse_lazy("userprofile:login")
    # 模板文件
    template_name = "article/create.html"
    # 模型类
    model = ArticlePost
    # 发表文章所需字段
    fields = ["author", "title", "body"]

    # 成功发表文章后跳转地址
    def get_success_url(self):
        return reverse_lazy('article:detail', kwargs={'id': self.object.id})


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    # 登录链接
    login_url = reverse_lazy("userprofile:login")
    template_name = "article/update.html"
    model = ArticlePost
    pk_url_kwarg = 'id'
    fields = ["title", "body"]

    def get_success_url(self):
        return reverse_lazy('article:detail', kwargs={'id': self.object.id})


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    # 登录链接
    login_url = reverse_lazy("userprofile:login")
    model = ArticlePost
    pk_url_kwarg = "id"
    success_url = reverse_lazy("article:article_list")


@csrf_exempt
def upload_img(request):
    if request.method == "POST":
        file = request.FILES["upload"]
        file_name = file.name
        auth = oss2.Auth(settings.OSS_KEY, settings.OSS_SECRET)
        bucket = oss2.Bucket(auth, settings.OSS_NODE, settings.OSS_BUCKET)
        resp = bucket.put_object(f"{settings.OSS_DIR}/{file_name}", file.read())
        print(resp.resp.response.url)
        result = {
            "fileName": file_name,
            "uploaded": 1,
            "url": resp.resp.response.url
        }
        return JsonResponse(result)

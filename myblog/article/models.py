from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class ArticlePost(models.Model):
    # 文章作者
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    # 文章标题
    title = models.CharField(max_length=100, verbose_name="文章标题")
    # 文章正文
    body = models.TextField()
    # 文章创建时间
    created = models.DateTimeField(default=timezone.now, verbose_name="文章创建时间")
    # 文章修改时间
    updated = models.DateTimeField(auto_now=True, verbose_name="文章更新时间")
    # 文章浏览量
    total_views = models.PositiveIntegerField(default=0, verbose_name="文章浏览量")

    class Meta:
        ordering = ('-created', )
        verbose_name = verbose_name_plural = "文章"

    def __str__(self):
        return self.title


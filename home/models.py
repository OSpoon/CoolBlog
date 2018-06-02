from django.db import models

# Create your models here.

class Category(models.Model):

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = "分类列表"  # verbose_name

    #分类名称
    name = models.CharField(max_length=50,verbose_name="分类名称")

class Tag(models.Model):

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = "标签列表"  # verbose_name

    # 名称
    name = models.CharField(max_length=50,verbose_name="标签名称")

class Article(models.Model):

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = "文章列表"

    # 文章标题
    title = models.CharField(max_length=70,verbose_name="文章标题")
    #文章内容
    body = models.TextField(verbose_name="文章内容",default='')
    #创建时间
    created_time = models.DateTimeField(verbose_name="创建时间")
    # 修改时间
    modified_time = models.DateTimeField(verbose_name="修改时间")
    # 摘要
    excerpt = models.CharField(max_length=200, blank=True,verbose_name="摘要")
    # 分类
    category = models.ForeignKey(Category,verbose_name="分类")
    # 标签
    tags = models.ManyToManyField(Tag, blank=True,verbose_name=u"标签")
    # 作者
    # author = models.ForeignKey(User,verbose_name="作者")
    #浏览量
    # views = models.PositiveIntegerField(defalut=0,verbose_name="浏览量")
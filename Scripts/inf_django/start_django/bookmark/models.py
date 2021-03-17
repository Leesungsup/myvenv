from django.db import models
from django.urls import reverse
# Create your models here.
class Bookmark(models.Model):
    site_name=models.CharField(max_length=100)
    url=models.URLField('Site url')
    #필드의 종류가 결정하는 것 컬럼,제약사항,Form의 종류, 제약사항
    def __str__(self):
        return "이름 : "+self.site_name+" 주소 : "+self.url
    def get_absolute_url(self):
        return reverse('detail',args=[str(self.id)])

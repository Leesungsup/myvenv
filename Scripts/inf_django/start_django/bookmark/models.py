from django.db import models

# Create your models here.
class Bookmark(models.Model):
    site_name=models.CharField(max_length=100)
    url=models.URLField('Site url')
    #필드의 종류가 결정하는 것 컬럼,제약사항,Form의 종류, 제약사항
    

from django.db import models
class Question(models.Model):
    question_text=models.TextField();
    date=models.DateTimeField('date published')
     def __str__(self):  # __unicode__ on Python 2
        return self.question_text

class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    def __self__(self):
        retunr self.choice_text

# Create your models here.

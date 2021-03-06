from random import choice
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    slug=models.SlugField()
    content=models.CharField(max_length=1024)

    def __str__(self):
        return self.content
        
class Answer(models.Model):
  question = models.ForeignKey('Question', on_delete = models.CASCADE)
  choice = models.ForeignKey('Choice', on_delete = models.CASCADE)
  user = models.ForeignKey(User, on_delete = models.CASCADE)

class Choice(models.Model):
    question=models.ForeignKey('Question', on_delete=models.CASCADE)
    choice=models.CharField(max_length=256)
    @property
    def answer_count(self):
        return Answer.objects.filter(
            question=self.question,
            choice=self.id
        ).count()
    def __str__(self):
        return "{}--{}".format(self.question.content[:100],self.choice)





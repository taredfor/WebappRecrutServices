from django.db import models
import datetime
from django.utils import timezone


# Create your models here.
class Questions(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField("date published")

    def __str__(self):
        return self.question_text

    def was_published(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Person(models.Model):
    f_name = models.CharField(max_length=20)
    s_name = models.CharField(max_length=20)
    planet = models.CharField(max_length=20)
    objects = models.Manager()


class ObjectRecruts(models.Model):
    f_name = models.CharField(max_length=20)
    s_name = models.CharField(max_length=20)
    age = models.IntegerField()
    mail_address = models.EmailField()
    planet = models.CharField(max_length=20)
    objects = models.Manager()


class ObjectsPlanet(models.Model):
    planet = models.CharField(max_length=20)


class ObjectsSitx(models.Model):
    name = models.CharField(max_length=20)
    planet = models.ForeignKey(ObjectsPlanet, on_delete=models.CASCADE)


class ObjectsOrder(models.Model):
    order = models.CharField(max_length=20)


class ObjectsQuestion(models.Model):
    questions = models.CharField(max_length=50)
    answers = models.BooleanField(default=True)
    objects = models.Manager()

    def get_all(self):
        self.questions = ObjectsQuestion.objects.all()


class ObjectsAnswers(models.Model):
    user_id = models.IntegerField()
    questions = models.IntegerField(null=True)
    answers = models.BooleanField(null=True)


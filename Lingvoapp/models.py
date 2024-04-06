from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Language(models.Model):
    language_id = models.AutoField(primary_key = True)
    language_name = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.language_name
    

class Unit(models.Model):
    unit_id = models.AutoField(primary_key=True)
    unit_name = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.unit_name
    

class UnitContent(models.Model):
    unitcontent_id = models.AutoField(primary_key=True)
    unit = models.ForeignKey(Unit,on_delete = models.CASCADE)
    wordsentence_id = models.IntegerField()
    english_words = models.CharField(max_length = 200)
    french_words = models.CharField(max_length = 200)
    spanish_words = models.CharField(max_length = 200)
    german_words = models.CharField(max_length = 200)
    hindi_words = models.CharField(max_length = 200)
    gujarati_words = models.CharField(max_length = 200)

    
class CourseRegistration(models.Model):
    coursereg_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    language = models.ForeignKey(Language,on_delete = models.CASCADE)
    unit = models.ForeignKey(Unit,on_delete = models.CASCADE)


class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    unit = models.ForeignKey(Unit,on_delete = models.CASCADE)
    english_question = models.CharField(max_length=500)
    french_question = models.CharField(max_length=500)
    german_question = models.CharField(max_length=500)
    spanish_question = models.CharField(max_length=500)
    hindi_question = models.CharField(max_length=500)
    gujarati_question = models.CharField(max_length=500)
    Score_per_que = models.IntegerField()


class Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question,on_delete = models.CASCADE)
    option_1 = models.CharField(max_length=200)
    option_2 = models.CharField(max_length=200)
    option_3 = models.CharField(max_length=200)
    option_4 = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length = 200)




from django.db import models

class Answers(models.Model):
    quiz = models.CharField(default=False, max_length=10)
    q1 = models.CharField(default=False, max_length=200)
    q2 = models.CharField(default=False, max_length=200)
    q3 = models.CharField(default=False, max_length=200)
    q4 = models.CharField(default=False, max_length=200)
    q5 = models.CharField(default=False, max_length=200)
    q6 = models.CharField(default=False, max_length=200)
    q7 = models.CharField(default=False, max_length=200)
    q8 = models.CharField(default=False, max_length=200)
    q9 = models.CharField(default=False, max_length=200)
    q10 = models.CharField(default=False, max_length=200)

    def __str__(self):
        return f'{self.quiz} Answers'

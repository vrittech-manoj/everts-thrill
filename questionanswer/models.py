from django.db import models
import uuid
from django.utils.text import slugify

# Create your models here.
class Question(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    question_title = models.CharField(max_length = 450)
    status = models.BooleanField(default = True)
    position = models.PositiveIntegerField(default = 999)
    
    def __str__(self):
        return self.title
    
class QuestionHaveAnswer(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    answer_title = models.CharField(max_length = 450)
    status = models.BooleanField(default = True)
    position = models.PositiveIntegerField(default = 1)
    question = models.OneToOneField(Question,related_name = "answer",on_delete = models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.position = int(QuestionHaveAnswer.objects.last().position)+1
        super().save(*args, **kwargs)

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)

class Test(models.Model):
    title = models.CharField(max_length=100)
    duration = models.IntegerField()  # in minutes
    total_questions = models.IntegerField()
    total_marks = models.IntegerField()
    negative_marks = models.BooleanField(default=False)
    sections = models.IntegerField(default=1)

    def __str__(self):
        return self.title

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    text = models.TextField()
    is_mcq = models.BooleanField(default=True)
    option1 = models.CharField(max_length=200, blank=True)
    option2 = models.CharField(max_length=200, blank=True)
    option3 = models.CharField(max_length=200, blank=True)
    option4 = models.CharField(max_length=200, blank=True)
    correct_answer = models.CharField(max_length=200, blank=True)
    marks = models.IntegerField(default=1)

    def __str__(self):
        return self.text[:50]

    @property
    def user_response(self):
        try:
            return UserResponse.objects.get(question=self)
        except UserResponse.DoesNotExist:
            return None

class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField(blank=True)
    is_correct = models.BooleanField(default=False)
    marked_for_review = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'test', 'question')

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    rating = models.IntegerField(null=True, blank=True)
    experience = models.IntegerField(null=True, blank=True)
    quality = models.IntegerField(null=True, blank=True)
    difficulty = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
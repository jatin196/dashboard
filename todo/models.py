from django.db import models
from django.shortcuts import render, reverse
from django.contrib.auth import get_user_model

class Task(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=65)
    desc = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField()

    def __str__(self):
        return self.title

    def delete_url(self):
        return reverse('delete', kwargs={
            'id': self.id
        })
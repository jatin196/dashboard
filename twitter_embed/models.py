from django.db import models
from embed_video.fields import EmbedVideoField


class item(models.Model):
    video = EmbedVideoField()
from django.db import models

class BreakoutRoom(models.Model):
    topic = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic


class Participant(models.Model):
    breakout_room = models.ForeignKey(BreakoutRoom, on_delete=models.CASCADE, related_name="participants")
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
from django.db import models

class RequestLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    request_data = models.JSONField()
    response_data = models.JSONField()
    turnaround_time = models.FloatField()

    def __str__(self):
        return str(self.turnaround_time)

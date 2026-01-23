from django.conf import settings
from django.db import models

class Attendance(models.Model):
    STATUS_CHOICES = (
        ("PRESENT", "Present"),
        ("ABSENT", "Absent"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.user.email} - {self.date} - {self.status}"

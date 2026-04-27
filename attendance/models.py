from django.db import models
from accounts.models import User


class Attendance(models.Model):
    employee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="attendance_records"
    )

    date = models.DateField(auto_now_add=True)

    status = models.CharField(
    max_length=10,
    choices=[
        ("PRESENT", "Present"),
        ("ABSENT", "Absent"),
        ("LATE", "Late"),
    ]
)

    def __str__(self):
        return f"{self.employee.email} - {self.date} - {self.status}"
from django.db import models
from accounts.models import User


class Attendance(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=[("Present", "Present"), ("Absent", "Absent")],
        default="Present"
    )

    class Meta:
        #unique_together = ("employee", "date")

    def __str__(self):
        return f"{self.employee.email} - {self.date} - {self.status}"
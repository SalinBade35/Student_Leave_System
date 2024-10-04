from django.db import models

class StudentLeave(models.Model):
    roll_number = models.CharField(max_length=6, unique=True)
    full_name = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    semester = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    leave_type = models.CharField(max_length=50)
    reason = models.TextField()
    document = models.FileField(upload_to='documents/', blank=True, null=True)
    guardian_contact = models.CharField(max_length=15)
    student_contact = models.CharField(max_length=15)




from django.db import models

# Create your models here.
GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
]
EMPLOYMENT_STATUS_CHOICES = [
    ('active', 'Active'),
    ('inactive', 'Inactive'),
    ('terminated', 'Terminated'),
    ('resigned', 'Resigned'),
]

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    manager = models.OneToOneField('Staff', on_delete=models.SET_NULL, null=True, blank=True, related_name='manages')
    def __str__(self):
        return self.name
class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name

class Staff(models.Model):
    staff_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"ID: {self.staff_id}, Name: {self.name}, Position: {self.position}, Salary: ${self.salary}"

class Shift(models.Model):
    name = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name


class ShiftAssignment(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='shifts')
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE, related_name='assignments')
    date = models.DateField()
    class Meta:
        unique_together = ('staff', 'shift', 'date')
    def __str__(self):
        return f"{self.staff} assigned to {self.shift} on {self.date}"
    
class Attendance(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name="attendance")
    date = models.DateField()
    check_in = models.TimeField()
    check_out = models.TimeField(blank=True, null=True)
    shift = models.ForeignKey(Shift, on_delete=models.SET_NULL, null=True, blank=True)
    remarks = models.TextField(blank=True, null=True)
    class Meta:
        unique_together = ('staff', 'date')
    def __str__(self):
        return f"Attendance for {self.staff} on {self.date}"


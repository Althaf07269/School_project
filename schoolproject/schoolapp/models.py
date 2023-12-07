from django.db import models
from django.urls import reverse

class Course(models.Model):
    name = models.CharField(max_length=250)
    des = models.TextField()
    duration = models.CharField(max_length=20)
    img = models.ImageField(upload_to='photo')
    link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('all_courses', args=[str(self.id)])

from django.db import models

class EnquiryForm(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    mail_id = models.EmailField()
    address = models.TextField()
    department_name = models.CharField(max_length=100, null=True)  # Field for department name
    course_name = models.CharField(max_length=100, null=True)  # Field for course name
    purpose = models.CharField(max_length=100)
    materials_provide = models.TextField()

    def __str__(self):
        return self.name




from django.db import models

class Departments(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()

    def __str__(self):
        return self.dep_name


class Doctors(models.Model):
    doc_name = models.CharField(max_length=225)
    doc_spec = models.CharField(max_length=225)
    dep_name = models.ForeignKey(Departments, on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to='doctors')

    def __str__(self):
        return f"Dr. {self.doc_name} ({self.doc_spec})"


class Booking(models.Model):
    p_name = models.CharField(max_length=225)
    p_phone = models.CharField(max_length=15)
    p_email = models.EmailField()
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)  # Correct field name
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now_add=True)  # auto_now_add for creation date

    def __str__(self):
        return f"{self.p_name} booked Dr. {self.doctor.doc_name} on {self.booking_date}"

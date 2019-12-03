from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Patient(models.Model):
    ON = 0
    OP = 1
    AN = 2
    AP = 3
    BN = 4
    BP = 5
    ABP = 6
    ABN = 7
    BLOOD_TYPES = (
        (ON, 'o-'),
        (OP, 'o+'),
        (AN, 'a-'),
        (AP, 'a+'),
        (BN, 'b-'),
        (BP, 'b+'),
        (ABP, 'ab+'),
        (ABN, 'ab-')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    bloodType = models.IntegerField(choices=BLOOD_TYPES, null=False)
    height = models.DecimalField(max_digits=3, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)

class SkinImages(models.Model):
    patient_key = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    image = models.ImageField(upload_to="skin_imgs/", default = 'skin_imgs/None/no-img.jpg')
    objects = models.Manager()
    def __str__(self):
        return self.title


class Diagnostics(models.Model):
    patient_key = models.ForeignKey(User, on_delete=models.CASCADE)
    image_key = models.ForeignKey(SkinImages, on_delete=models.CASCADE)
    diagnostic = models.CharField(max_length=64)
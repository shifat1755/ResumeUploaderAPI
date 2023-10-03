from django.db import models


STATE_CHOISE=(
    ("Khulna","Khulna"),
    ("Dhaka","Dhaka"),
    ("Rajshahi","Rajshahi"))

class Profile(models.Model):
    name=models.CharField(max_length=500)
    email=models.EmailField()
    dob=models.DateField(auto_now=False,auto_now_add=False)
    state=models.CharField(choices=STATE_CHOISE, max_length=50)
    gender=models.CharField(max_length=10)
    location=models.CharField(max_length=100)
    pimage=models.ImageField(upload_to='pimages',blank=True)
    rdoc=models.FileField(upload_to='rdocs',blank=True)
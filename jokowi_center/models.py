from django.db import models

# Create your models here.
class Blog(models.Model):
    judul=models.CharField(max_length=200)
    gambar=models.CharField(max_length=200)
    isi=models.TextField()
    date =models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.judul

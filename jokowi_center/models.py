from django.db import models

# Create your models here.
class Masukan (models.Model):
    nama_lengkap = models.CharField(max_length=225)
    alamat_email = models.CharField(max_length=225)
    judul = models.CharField(max_length=100)
    isi_pesan = models.TextField()
    def __str__(self):
        return self.nama_lengkap

class Blog(models.Model):
    judul=models.CharField(max_length=200)
    gambar=models.CharField(max_length=200)
    isi=models.TextField()
    date =models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.judul

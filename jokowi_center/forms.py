from django import forms

from .models import Masukan

class Inputfeedback(forms.ModelForm):

    class Meta:
        model = Masukan
        fields = ('nama_lengkap', 'alamat_email','judul','isi_pesan',)

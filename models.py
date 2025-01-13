from django.db import models

class Pronat(models.Model):
    pronat_emri = models.CharField(max_length=100,null=True,blank=True)
    pronat_pershkrimi = models.TextField(max_length=1000000,null=True,blank=True)
    pronat_imazhi = models.ImageField(upload_to="pronat/" ,null=True,blank=True)
    pronat_cmimi = models.DecimalField(max_digits=20, decimal_places=2, null=True,blank=True) #549.99

from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nomi")
    price = models.IntegerField(verbose_name="Narxi (som)")
    ram = models.CharField(max_length=20, verbose_name="RAM")
    storage = models.CharField(max_length=20, verbose_name="Xotira")
    camera = models.CharField(max_length=50, verbose_name="Kamera", blank=True)
    battery = models.CharField(max_length=50, verbose_name="Batareya", blank=True)
    description = models.TextField(verbose_name="Qoshimcha ma'lumot", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Telefon"
        verbose_name_plural = "Telefonlar"
        ordering = ["price"]

    def __str__(self):
        return f"{self.name} - {self.price:,} som"
    
    
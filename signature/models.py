from users.models import CustomUser
from django.db import models
from PIL import Image
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

class SignatureTool(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False)
    full_name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media_pics/', blank=True, default='default.jpg')

    facebook = models.CharField(max_length=50, blank=True, null=True)
    linkedin = models.CharField(max_length=50, blank=True, null=True)
    twitter = models.CharField(max_length=50, blank=True, null=True)
    github = models.CharField(max_length=50, blank=True, null=True)
    instagram = models.CharField(max_length=50, blank=True, null=True)
    whatsapp = models.CharField(max_length=50, blank=True, null=True)
    youtube = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'SignatureTool'
        verbose_name_plural = 'SignatureTool'
    def __str__(self):
        return f"{self.user.username}'s Signature"

@receiver(post_save, sender=CustomUser)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        SignatureTool.objects.create(user=instance)
    instance.signaturetool.save()
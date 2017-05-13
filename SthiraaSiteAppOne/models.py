from django.db import models
import uuid
# from django.utils.encoding import python_2_unicode_compatible

# @python_2_unicode_compatible
class article(models.Model):
    aid = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=800, blank=True, default='')
    author = models.CharField(max_length=200, blank=True, default='')
    date = models.DateField(auto_now=False, auto_now_add=False)
    photo = models.ImageField(upload_to='aimages/', height_field=None, width_field=None, max_length=100)
    content = models.FileField(upload_to='documents/', max_length=100)


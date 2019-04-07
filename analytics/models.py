from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType 
from django.contrib.sessions.models import Session 
from django.db.models.signals import pre_save, post_save 

from . import  utils
from .signals import object_viewed_signal


User = settings.AUTH_USER_MODEL

class ObjectViewed(models.Model):
    user = models.ForeignKey(User, blank=True, null = True, on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=220, blank=True, null=True)
    content_type = models.ForeignKey(ContentType,  on_delete=models.CASCADE) #User, product, order, cart, address
    object_id = models.PositiveIntegerField() # Product id, user id, order id
    content_object = GenericForeignKey('content_type', 'object_id') # product instance 
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} viewed {}".format(self.content_object, self.timestamp)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Object viewed'
        verbose_name_plural = 'Objects viewed'

def object_viewed_receiver(sender, instance, request, *args, **kwargs):
    c_type = ContentType.Objects.get_from_model(sender)
    new_view_obj = ObjectViewed.objects.create(
        user=request.user,
        content_type=c_type,
        object_id=instance.id,
        ip_address=get_client_ip(request)
    )

object_viewed_signal.connect(object_viewed_receiver)

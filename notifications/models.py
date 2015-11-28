from django.conf import settings
from django.db import models


class DeviceManager(models.Manager):
    def register_device(self, device_token, device_type, user):
        """
        Register device of type `device_type` using `device_token` it provided.
        Mark it as recently used by `user`, which means when sending a notification
        to the user, it will be sent to this device.

        Returns a 2-tuple: (success, device_id).
        """
        try:
            dev = Device.objects.get(device_token=device_token)

            if not dev.is_active:
                return False, None

            dev.user = user
            dev.save()
        except Device.DoesNotExist:
            dev = Device.objects.create(device_token=device_token,
                                        device_type=device_type,
                                        user=user
                                        )

        return True, dev.pk


class Device(models.Model):
    device_token = models.CharField(max_length=128,
                                    db_index=True,
                                    help_text='Device token used for notifications')
    device_type = models.CharField(max_length=32,
                                   blank=False
                                   )
    first_registered_at = models.DateTimeField(auto_now_add=True,
                                               help_text='Date and time when the device was first registered'
                                               )
    last_login_at = models.DateTimeField(auto_now=True,
                                         help_text='Date and time when the device was last used to log in'
                                         )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             verbose_name='Last used by',
                             related_name='devices',
                             help_text='Employee that last logged in using this device'
                             )
    is_active = models.BooleanField(default=True,
                                    help_text='If checked, the device will receive notifications'
                                    )
    objects = DeviceManager()

    def __unicode__(self):
        if not self.user:
            return self.device_type
        else:
            return u'{}: {}'.format(self.device_type, self.user)

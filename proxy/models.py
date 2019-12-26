from django.db import models


class Host(models.Model):
    resource = models.ForeignKey('Resource',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)
    host = models.URLField(null=True, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.host} ({self.resource.name})'


class NetSelect(models.Model):
    host = models.ForeignKey('Host',
                             null=True,
                             blank=True,
                             on_delete=models.SET_NULL)
    speed = models.IntegerField(default=0, help_text='In milliseconds')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.host} {self.speed} ms'


class Resource(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} ({self.url})'

from django.db import models


class TimeStampedModel(models.Model):
    """
    A class that provides self-updating `created` and `modified` fields on any model that inherits from it.

    Will be inhereted by all models in this project.
    """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        # Setting `abstract = True` will make sure that TimeStampedModel will not be used to create any database tables
        abstract = True

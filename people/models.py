from django.db import models


class Person(models.Model):
    sam_account_name    = models.CharField(max_length=200, unique=True)
    display_name        = models.CharField(max_length=200, null=True)
    is_manager          = models.NullBooleanField()
    photo_number        = models.IntegerField(null=True)

    def __str__(self):
        return self.sam_account_name


class Leave(models.Model):
    total       = models.IntegerField()
    days_left   = models.IntegerField()
    person_id   = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.days_left

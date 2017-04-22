from django.db import models


class Person(models.Model):
    id                  = models.AutoField(primary_key=True)
    sam_account_name    = models.CharField(max_length=200, unique=True)
    display_name        = models.CharField(max_length=200, null=True)
    is_manager          = models.NullBooleanField()
    photo_number        = models.BigIntegerField(null=True)

    def __str__(self):
        return self.sam_account_name

    @classmethod
    def addPersonFromCSV(self, row):
        if row['photoNumber'] != 'NULL':
            number = int(row['photoNumber'])
        else:
            number = None
        self.objects.filter(sam_account_name=row['samAccountName']).update_or_create(
            sam_account_name=row['samAccountName'], defaults={
                'photo_number': number
            }
        )




class Leave(models.Model):
    total       = models.IntegerField()
    days_left   = models.IntegerField()
    person      = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.days_left

class PhotoNumberRecord(models.Model):
    person_id = models.IntegerField()
    photo_number = models.IntegerField()


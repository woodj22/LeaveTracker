from django.db import models

class Person(models.Model):
    id                  = models.AutoField(primary_key=True)
    sam_account_name    = models.CharField(max_length=200, unique=True)
    display_name        = models.CharField(max_length=200, null=True, blank=True)
    is_manager          = models.NullBooleanField(blank=True)
    photo_number        = models.BigIntegerField(null=True, blank=True)
    sur_name            = models.CharField(max_length=255, blank=True)
    given_name          = models.CharField(max_length=255, blank=True)
    department          = models.CharField(max_length=255, blank=True)
    division            = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.sam_account_name

    @classmethod
    def addPeopleFromCSV(cls, csv):
        print(csv)
        for row in csv:
            number = cls.__sanitizeCsvData(row)

            cls.objects.filter(sam_account_name=row['samAccountName']).update_or_create(
                sam_account_name=row['samAccountName'], defaults={
                    # 'display_name':row['displayName'],
                    # 'sur_name':row['surname'],
                    # 'given_name':row['givenName'],
                    # 'department':row['department'],
                    # 'division':row['division'],
                    'photo_number': number
                }
            )

    @classmethod
    def __sanitizeCsvData(cls, row):
        return int(row['photoNumber']) if row['photoNumber'] != 'NULL' else None


class Leave(models.Model):
    total       = models.IntegerField()
    days_left   = models.IntegerField()
    person      = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.days_left


class PhotoNumberRecord(models.Model):
    sam_account_name = models.CharField(max_length=200, unique=True)
    photo_number = models.IntegerField()



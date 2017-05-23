from django.db import models


class Person(models.Model):
    id                  = models.AutoField(primary_key=True)
    samAccountName    = models.CharField(max_length=200, unique=True, db_column='sam_account_name')
    displayName        = models.CharField(max_length=200, null=True, blank=True, db_column = 'display_name')
    isManager          = models.NullBooleanField(blank=True,  db_column='is_manager')
    photoNumber        = models.BigIntegerField(null=True, blank=True, db_column='photo_number')
    surname            = models.CharField(max_length=255, blank=True, db_column='sur_name')
    givenName          = models.CharField(max_length=255, blank=True, db_column='given_name')
    department          = models.CharField(max_length=255, blank=True)
    division            = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.sam_account_name

    @classmethod
    def addPeopleFromCSV(cls, csv):

        for row in csv:
            default_values = cls.__sanitizeCsvData(row)
            cls.objects.filter(samAccountName=row['samAccountName']).update_or_create(
                 samAccountName=row['samAccountName'], defaults=default_values
            )

    @classmethod
    def __sanitizeCsvData(cls, row):
        sanatized_data = {
            'samAccountName' : row['samAccountName'],
            'displayName' : row['displayName'],
            'photoNumber' : int(row['photoNumber']) if row['photoNumber'] != 'NULL' else None,
            'surname' : row['surname'],
            'givenName' : row['givenName'],
            'department' : row['department'],
            'division' : row['division'],

        }
        return sanatized_data


class Leave(models.Model):
    total       = models.IntegerField()
    days_left   = models.IntegerField()
    person      = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.days_left


class PhotoNumberRecord(models.Model):
    sam_account_name = models.CharField(max_length=200, unique=True)
    photo_number = models.IntegerField()

class Cms(models.Model):
    id = models.AutoField(primary_key=True)
    HRNumber = models.CharField(max_length=200, unique=True)
    ExternalID = models.CharField(max_length=200)
    PersonID = models.BigIntegerField(null=True, blank=True)
    LastName = models.CharField(max_length=200)
    FirstName = models.CharField(max_length=200)
    AffiliationID = models.CharField(max_length=200)
    BuildingID = models.CharField(max_length=200)
    VehicleRegNo = models.BigIntegerField(null=True, blank=True)
    PinCode = models.BigIntegerField(null=True, blank=True)
    ServicePartnerID = models.BigIntegerField(null=True, blank=True)
    CompanyName = models.CharField(max_length=200)
    CostCode = models.CharField(max_length=200)
    SupervisorID = models.BigIntegerField(null=True, blank=True)
    HRNumber = models.BigIntegerField(null=True, blank=True)
    PersonnelOfficerCode = models.CharField(max_length=200)
    Department = models.CharField(max_length=200)
    Division = models.CharField(max_length=200)
    CreationDate = models.BigIntegerField(null=True, blank=True)
    CreatedBy = models.CharField(max_length=200)
    ModifiedDate = models.BigIntegerField(null=True, blank=True)
    ModifiedBy = models.BigIntegerField(null=True, blank=True)
    IsArchived = models.BigIntegerField(null=True, blank=True)
    LoginID = models.BigIntegerField(null=True, blank=True)
    ExternalID = models.BigIntegerField(null=True, blank=True)
    ExportFlag = models.CharField(max_length=200)
    IsInDiamond = models.CharField(max_length=200)
    SentryID = models.CharField(max_length=200)
    FCWnxExportFlag = models.CharField(max_length=200)
    FCWnxLastExportDate = models.CharField(max_length=200)

    @classmethod
    def addPeopleFromCSV(cls, csv):
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


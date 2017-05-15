# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-15 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20170512_0859'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cms',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('PersonID', models.BigIntegerField(blank=True, null=True)),
                ('LastName', models.CharField(max_length=200)),
                ('FirstName', models.CharField(max_length=200)),
                ('AffiliationID', models.CharField(max_length=200)),
                ('BuildingID', models.CharField(max_length=200)),
                ('VehicleRegNo', models.BigIntegerField(blank=True, null=True)),
                ('PinCode', models.BigIntegerField(blank=True, null=True)),
                ('ServicePartnerID', models.BigIntegerField(blank=True, null=True)),
                ('CompanyName', models.CharField(max_length=200)),
                ('CostCode', models.CharField(max_length=200)),
                ('SupervisorID', models.BigIntegerField(blank=True, null=True)),
                ('HRNumber', models.BigIntegerField(blank=True, null=True)),
                ('PersonnelOfficerCode', models.CharField(max_length=200)),
                ('Department', models.CharField(max_length=200)),
                ('Division', models.CharField(max_length=200)),
                ('CreationDate', models.BigIntegerField(blank=True, null=True)),
                ('CreatedBy', models.CharField(max_length=200)),
                ('ModifiedDate', models.BigIntegerField(blank=True, null=True)),
                ('ModifiedBy', models.BigIntegerField(blank=True, null=True)),
                ('IsArchived', models.BigIntegerField(blank=True, null=True)),
                ('LoginID', models.BigIntegerField(blank=True, null=True)),
                ('ExternalID', models.BigIntegerField(blank=True, null=True)),
                ('ExportFlag', models.CharField(max_length=200)),
                ('IsInDiamond', models.CharField(max_length=200)),
                ('SentryID', models.CharField(max_length=200)),
                ('FCWnxExportFlag', models.CharField(max_length=200)),
                ('FCWnxLastExportDate', models.CharField(max_length=200)),
            ],
        ),
    ]

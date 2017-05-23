# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-23 20:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('days_left', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('samAccountName', models.CharField(db_column=b'sam_account_name', max_length=200, unique=True)),
                ('displayName', models.CharField(blank=True, db_column=b'display_name', max_length=200, null=True)),
                ('isManager', models.NullBooleanField(db_column=b'is_manager')),
                ('photoNumber', models.BigIntegerField(blank=True, db_column=b'photo_number', null=True)),
                ('surName', models.CharField(blank=True, db_column=b'sur_name', max_length=255)),
                ('givenName', models.CharField(blank=True, db_column=b'given_name', max_length=255)),
                ('department', models.CharField(blank=True, max_length=255)),
                ('division', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PhotoNumberRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sam_account_name', models.CharField(max_length=200, unique=True)),
                ('photo_number', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='leave',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Person'),
        ),
    ]

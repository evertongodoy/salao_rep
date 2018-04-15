# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('EMPLOYEE_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('FIRST_NAME', models.CharField(max_length=20)),
                ('LAST_NAME', models.CharField(max_length=25)),
                ('EMAIL', models.CharField(max_length=25)),
                ('PHONE_NUMBER', models.CharField(max_length=20)),
                ('HIRE_DATE', models.DateField()),
                ('JOB_ID', models.CharField(max_length=10)),
                ('SALARY', models.FloatField()),
                ('COMMISSION_PCT', models.FloatField()),
                ('MANAGER_ID', models.IntegerField()),
                ('DEPARTMENT_ID', models.IntegerField()),
            ],
            options={
                'db_table': 'employees',
            },
        ),
    ]

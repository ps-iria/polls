# Generated by Django 2.2 on 2021-07-02 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210702_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='start_date',
            field=models.DateField(),
        ),
    ]

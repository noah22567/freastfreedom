# Generated by Django 2.2.2 on 2019-06-17 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0003_auto_20190617_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitchen',
            name='Kitchenimg',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]

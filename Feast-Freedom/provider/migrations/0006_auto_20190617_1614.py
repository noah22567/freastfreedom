# Generated by Django 2.2.2 on 2019-06-17 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0005_auto_20190617_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitchen',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider.ServiceProvider'),
        ),
    ]

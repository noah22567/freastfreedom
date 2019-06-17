# Generated by Django 2.2.2 on 2019-06-17 13:55

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('users', '0005_delete_myuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='myUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_provider', models.BooleanField(default=False, verbose_name='provider')),
                ('securityquestion1', models.CharField(max_length=20, verbose_name='Security question 1: What is the name of hospital were you born in?')),
                ('securityquestion2', models.CharField(max_length=20, verbose_name='Security question 2: What was your childhood friends name?')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-07 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_userwallet_private_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='userwallet',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 5.0.6 on 2024-10-02 07:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='group',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='group', to='group.group'),
            preserve_default=False,
        ),
    ]

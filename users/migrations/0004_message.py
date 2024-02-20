# Generated by Django 5.0.1 on 2024-02-08 12:12

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_location_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('subject', models.CharField(blank=True, max_length=255, null=True)),
                ('body', models.TextField()),
                ('is_read', models.BooleanField(default=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('recipient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messages', to='users.profile')),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile')),
            ],
            options={
                'ordering': ['-is_read', '-created'],
            },
        ),
    ]

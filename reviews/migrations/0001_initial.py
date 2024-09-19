# Generated by Django 5.1.1 on 2024-09-18 02:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stays', '0003_remove_host_gender_remove_host_rating_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('comments', models.CharField(max_length=255)),
                ('property', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='stays.stay')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

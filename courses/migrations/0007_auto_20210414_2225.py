# Generated by Django 3.2 on 2021-04-14 16:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0006_assignment'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='subject',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='courses.subject'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assignment',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments_created', to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 2.2.24 on 2021-09-06 10:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('package', '0005_auto_20190927_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='date_deprecated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='deprecated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='deprecator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='package',
            name='deprecates_package',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='replacement', to='package.Package'),
        ),
    ]
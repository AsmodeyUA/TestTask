# Prepared by AsmodeyZ 04092018
from django.conf import settings
from django.db import migrations, models
from django.contrib.auth.models import User


def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    db_alias = schema_editor.connection.alias
    User.objects.using(db_alias).bulk_create([
        User(username="autouser1"),
        User(username="autouser2"),
    ])


def reverse_func(apps, schema_editor):
    # forwards_func() creates two User instances,
    # so reverse_func() should delete them.
    db_alias = schema_editor.connection.alias
    User.objects.using(db_alias).filter(username="autouser1").delete()
    User.objects.using(db_alias).filter(username="autouser2").delete()


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
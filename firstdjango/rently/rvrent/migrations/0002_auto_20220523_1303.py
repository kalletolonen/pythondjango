# Generated by Django 3.2 on 2022-05-23 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rvrent', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rv',
            old_name='name',
            new_name='vehicle',
        ),
        migrations.RemoveField(
            model_name='rv',
            name='reqLicense',
        ),
        migrations.AddField(
            model_name='rv',
            name='requiredLicence',
            field=models.CharField(choices=[('b', 'B'), ('be', 'BE'), ('c', 'C'), ('ce', 'CE'), ('d', 'D'), ('de', 'DE'), ('e', 'E')], default='b', max_length=6),
        ),
    ]
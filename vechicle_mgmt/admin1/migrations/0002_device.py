# Generated by Django 4.0.1 on 2022-01-19 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev_name', models.CharField(max_length=120, unique=True)),
                ('imei', models.CharField(max_length=15)),
                ('p_sim', models.IntegerField(max_length=10)),
                ('s_sim', models.IntegerField(max_length=10)),
                ('status', models.CharField(choices=[('bios', 'bios'), ('uefi', 'uefi'), ('ssd', 'ssd')], default='bios', max_length=120)),
            ],
        ),
    ]

# Generated by Django 2.2.1 on 2019-05-31 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colonias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('codigopostal', models.IntegerField(verbose_name=5)),
                ('referencias', models.CharField(max_length=90)),
            ],
        ),
    ]
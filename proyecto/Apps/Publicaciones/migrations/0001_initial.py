# Generated by Django 2.2.1 on 2019-05-31 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Usuarios', '0001_initial'),
        ('Colonias', '0001_initial'),
        ('Categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=150)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Categorias.Categorias')),
                ('colonia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Colonias.Colonias')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuarios.Usuarios')),
            ],
        ),
    ]

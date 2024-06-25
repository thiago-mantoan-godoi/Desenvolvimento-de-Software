# Generated by Django 3.1.2 on 2020-10-29 12:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.CharField(max_length=50)),
                ('nome', models.CharField(max_length=100)),
                ('descrição', models.CharField(max_length=250)),
                ('criada_em', models.DateTimeField(auto_now_add=True)),
                ('fechada_em', models.DateTimeField()),
                ('status', models.CharField(choices=[('1', 'Planejada'), ('2', 'Em Execução'), ('3', 'Concluída'), ('4', 'Cancelada')], max_length=1)),
                ('situacao', models.CharField(choices=[('1', 'Aberta'), ('2', 'Abandonada'), ('3', 'Fechada')], max_length=1)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tasks.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Execucao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.DateTimeField()),
                ('fim', models.DateTimeField()),
                ('tarefa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tasks.tarefa')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tasks.usuario')),
            ],
        ),
    ]

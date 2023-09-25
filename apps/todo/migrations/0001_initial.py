# Generated by Django 4.2.5 on 2023-09-25 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='описание')),
                ('completed', models.BooleanField(default=True, verbose_name='статус выполнения')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
            ],
            options={
                'verbose_name': 'Основные настройки',
                'verbose_name_plural': 'Основная настройка',
            },
        ),
    ]
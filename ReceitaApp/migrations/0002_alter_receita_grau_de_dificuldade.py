# Generated by Django 5.0.3 on 2024-04-03 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReceitaApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='grau_de_dificuldade',
            field=models.CharField(blank=True, choices=[('EAS', 'Easy'), ('INT', 'Intermediary'), ('DIF', 'Difficult')], max_length=10, null=True),
        ),
    ]

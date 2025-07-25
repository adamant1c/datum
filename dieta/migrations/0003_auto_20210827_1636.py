# Generated by Django 3.2.5 on 2021-08-27 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dieta', '0002_auto_20210827_1435'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dieta',
            options={'ordering': ['-data', 'nome_dieta'], 'verbose_name': 'Dieta', 'verbose_name_plural': 'Diete'},
        ),
        migrations.AlterModelOptions(
            name='ingrediente',
            options={'ordering': ['Nome'], 'verbose_name': 'Ingrediente', 'verbose_name_plural': 'Ingredienti'},
        ),
        migrations.AlterModelOptions(
            name='ingrediente_piatto',
            options={'ordering': ['Nome'], 'verbose_name': 'Ingrediente nel piatto', 'verbose_name_plural': 'Ingredienti nei piatti'},
        ),
        migrations.RemoveField(
            model_name='dieta',
            name='giorno_settimana',
        ),
        migrations.RemoveField(
            model_name='dieta',
            name='nome_piatto',
        ),
        migrations.RemoveField(
            model_name='dieta',
            name='tipo_pasto',
        ),
        migrations.AlterField(
            model_name='ingrediente_piatto',
            name='Piatto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dieta.piatti'),
        ),
        migrations.CreateModel(
            name='Tipo_Pasto_Piatto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dieta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dieta.dieta')),
                ('giorno_settimana', models.ManyToManyField(to='dieta.Giorno_settimana')),
                ('nome_piatto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dieta.piatto')),
                ('tipo_pasto', models.ManyToManyField(null=True, to='dieta.Tipo_pasto')),
            ],
            options={
                'verbose_name': 'Tipo-Pasto',
                'verbose_name_plural': 'Tipi-Pasto',
            },
        ),
    ]

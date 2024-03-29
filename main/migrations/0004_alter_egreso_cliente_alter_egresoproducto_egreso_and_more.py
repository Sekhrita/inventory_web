# Generated by Django 4.2.1 on 2023-07-21 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_egresoproducto_egreso_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='egreso',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.cliente'),
        ),
        migrations.AlterField(
            model_name='egresoproducto',
            name='egreso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.egreso'),
        ),
        migrations.AlterField(
            model_name='egresoproducto',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.producto'),
        ),
        migrations.AlterField(
            model_name='ingreso',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.proveedor'),
        ),
        migrations.AlterField(
            model_name='ingresoproducto',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.producto'),
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-09 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_usuario_rename_fecha_egreso_fechasistema_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='egreso',
            name='fechaMovimiento',
            field=models.DateTimeField(default=''),
        ),
        migrations.AlterField(
            model_name='ingreso',
            name='fechaMovimiento',
            field=models.DateTimeField(default=''),
        ),
        migrations.AlterField(
            model_name='producto',
            name='stock',
            field=models.PositiveBigIntegerField(default='0'),
        ),
    ]
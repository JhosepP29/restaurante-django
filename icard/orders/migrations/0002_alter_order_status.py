# Generated by Django 4.0.5 on 2022-07-03 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('PENDING', 'pending'), ('DELIVERED', 'delivered')], max_length=255),
        ),
    ]
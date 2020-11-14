# Generated by Django 3.1.3 on 2020-11-14 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pAuth', '0002_auto_20201113_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.TextField(default='', max_length=700),
        ),
        migrations.AddField(
            model_name='profile',
            name='mobile_no',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AddField(
            model_name='seller',
            name='company_name',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='product',
            name='sold_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pAuth.seller'),
        ),
    ]
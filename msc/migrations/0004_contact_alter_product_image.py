# Generated by Django 5.0.6 on 2024-07-27 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msc', '0003_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(default='', max_length=60)),
                ('phno', models.CharField(default='', max_length=60)),
                ('des', models.IntegerField(default='', max_length=600)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='msc/images'),
        ),
    ]

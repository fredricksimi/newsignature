# Generated by Django 3.2 on 2021-06-23 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signature', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signaturetool',
            name='facebook',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='signaturetool',
            name='github',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='signaturetool',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='media_pics/'),
        ),
        migrations.AlterField(
            model_name='signaturetool',
            name='instagram',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='signaturetool',
            name='linkedin',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='signaturetool',
            name='twitter',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='signaturetool',
            name='whatsapp',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='signaturetool',
            name='youtube',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]

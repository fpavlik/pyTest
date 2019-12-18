# Generated by Django 2.2.8 on 2019-12-18 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Square',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mass', models.IntegerField()),
                ('is_free', models.BooleanField()),
                ('row', models.IntegerField()),
                ('col', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flower_name', models.CharField(help_text='Name of flower type', max_length=20)),
                ('mass', models.IntegerField()),
                ('consumption', models.IntegerField(help_text='How much food does it takes')),
                ('lives', models.IntegerField(help_text='How long does it lives in tacts')),
                ('sex_time', models.IntegerField(help_text='in which tact it can do some bad staff)))')),
                ('seeds', models.IntegerField()),
                ('position', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='modeling.Square')),
            ],
        ),
    ]

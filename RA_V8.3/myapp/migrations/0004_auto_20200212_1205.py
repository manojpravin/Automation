# Generated by Django 3.0.2 on 2020-02-12 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20200131_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='braking_chartview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org', models.CharField(max_length=15)),
                ('Active', models.IntegerField()),
                ('Loggedin', models.IntegerField()),
                ('Percentage', models.CharField(max_length=5)),
                ('ReportWeek', models.IntegerField()),
                ('ReportYear', models.IntegerField()),
            ],
            options={
                'db_table': 'braking_chartview',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='datamonitor',
        ),
        migrations.DeleteModel(
            name='rawdata',
        ),
        migrations.RenameField(
            model_name='exceldata',
            old_name='Activeusers',
            new_name='Active',
        ),
        migrations.RenameField(
            model_name='exceldata',
            old_name='UserUsage',
            new_name='Usage',
        ),
        migrations.RenameField(
            model_name='exceldata',
            old_name='Weeknumber',
            new_name='Week',
        ),
        migrations.AddField(
            model_name='exceldata',
            name='Year',
            field=models.IntegerField(null=True),
        ),
    ]

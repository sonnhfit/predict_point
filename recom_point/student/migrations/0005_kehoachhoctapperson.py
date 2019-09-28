# Generated by Django 2.2.5 on 2019-09-28 03:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20190926_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeHoachHocTapPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hocky', models.IntegerField(default=0)),
                ('hocphan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.HocPhan')),
                ('sinhvien', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

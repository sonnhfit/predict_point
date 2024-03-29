# Generated by Django 2.2.5 on 2019-09-25 13:07

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='SinhVien',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('masv', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('gioi_tinh', models.BooleanField(default=False)),
                ('ngaysinh', models.DateField(auto_now=True)),
                ('dia_chi', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ChuongTrinhDaoTao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='HocPhan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_hp', models.CharField(max_length=255)),
                ('so_tc', models.IntegerField(default=0)),
                ('so_tiet_lt', models.IntegerField(default=0)),
                ('so_tiet_th', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Khoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_khoa', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Nganh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_nganh', models.CharField(max_length=255)),
                ('khoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Khoa')),
            ],
        ),
        migrations.CreateModel(
            name='Lop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenlop', models.CharField(max_length=255)),
                ('khoa_dao_tao', models.IntegerField(default=0)),
                ('nganh', models.ForeignKey(on_delete=255, to='student.Nganh')),
            ],
        ),
        migrations.CreateModel(
            name='Diem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hocky', models.IntegerField(default=0)),
                ('diem', models.FloatField(default=0)),
                ('hocphan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.ChuongTrinhDaoTao')),
                ('sinhvien', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='chuongtrinhdaotao',
            name='mahp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.HocPhan'),
        ),
        migrations.AddField(
            model_name='chuongtrinhdaotao',
            name='makhoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Khoa'),
        ),
        migrations.AddField(
            model_name='chuongtrinhdaotao',
            name='manganh',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Nganh'),
        ),
        migrations.AddField(
            model_name='sinhvien',
            name='lop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Lop'),
        ),
        migrations.AddField(
            model_name='sinhvien',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]

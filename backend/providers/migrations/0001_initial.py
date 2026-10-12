from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=30)),
                ('cnic', models.CharField(max_length=30)),
                ('service', models.CharField(choices=[('Plumbing','Plumbing'),('Electrician','Electrician'),('Cleaning','Cleaning'),('Painter','Painter'),('Car Repair','Car Repair'),('Care Services','Care Services'),('Tutor','Tutor'),('IT Support','IT Support')], max_length=50)),
                ('experience', models.PositiveIntegerField(default=0)),
                ('address', models.TextField()),
                ('skills', models.TextField(blank=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='providers/profile/')),
                ('cnic_front', models.ImageField(blank=True, null=True, upload_to='providers/cnic/')),
                ('cnic_back', models.ImageField(blank=True, null=True, upload_to='providers/cnic/')),
                ('certificate', models.FileField(blank=True, null=True, upload_to='providers/certificates/')),
                ('status', models.CharField(choices=[('pending','Pending Verification'),('approved','Approved'),('rejected','Rejected')], default='pending', max_length=20)),
                ('rejection_reason', models.TextField(blank=True)),
                ('verified_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='provider_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

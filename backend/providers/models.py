from django.contrib.auth.models import User
from django.db import models

class Provider(models.Model):
    SERVICE_CHOICES = [
        ('Plumbing','Plumbing'), ('Electrician','Electrician'), ('Cleaning','Cleaning'),
        ('Painter','Painter'), ('Car Repair','Car Repair'), ('Care Services','Care Services'),
        ('Tutor','Tutor'), ('IT Support','IT Support'),
    ]
    
    STATUS_CHOICES = [('pending','Pending Verification'), ('approved','Approved'), ('rejected','Rejected')]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='provider_profile')
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=30)
    cnic = models.CharField(max_length=30)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    experience = models.PositiveIntegerField(default=0)
    address = models.TextField()
    skills = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='providers/profile/', blank=True, null=True)
    cnic_front = models.ImageField(upload_to='providers/cnic/', blank=True, null=True)
    cnic_back = models.ImageField(upload_to='providers/cnic/', blank=True, null=True)
    certificate = models.FileField(upload_to='providers/certificates/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    rejection_reason = models.TextField(blank=True)
    verified_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return f'{self.full_name} - {self.service} ({self.status})'

    @property
    def is_verified(self):
        return self.status == 'approved'

class Booking(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    client_name = models.CharField(max_length=150)
    client_email = models.EmailField()
    client_phone = models.CharField(max_length=30)

    service = models.CharField(max_length=50, choices=Provider.SERVICE_CHOICES)

    booking_date = models.DateField()
    booking_time = models.TimeField()

    address = models.TextField()
    additional_details = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} - {self.service} - {self.status}"
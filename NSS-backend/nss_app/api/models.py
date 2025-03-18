from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_CHOICES = [
        ('Coordinator', 'Coordinator'),
        ('Slot Coordinator', 'Slot Coordinator'),
        ('Student', 'Student'),
        ('Admin', 'Admin'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    entry_number = models.CharField(max_length=20, blank=True, null=True)
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    webmail = models.EmailField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Slot Coordinator')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username}'s profile"

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='announcement_images', blank=True, null=True)
    
    def __str__(self):
        return self.title

class Download(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='downloads')
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100)
    uploaded_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Gallery(models.Model):
    TYPE_CHOICES = [
        ('regularclasses', 'Regular Classes'),
        ('doubts', 'Doubts'),
        ('exams', 'Exams'),
    ]

    title = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='regularclasses')
    year = models.IntegerField(default=2024)

    def __str__(self):
        return f"{self.title} - {self.location} ({self.year})"

class Brochure(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='brochures/')
    year = models.IntegerField(default=2024)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.year})"

    class Meta:
        ordering = ['-year', '-created_at']

class Report(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='reports/')
    year = models.IntegerField(default=2024)
    location = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.location} ({self.year})"

    class Meta:
        ordering = ['-year', '-created_at']

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        ordering = ['-created_at']

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='event_images', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} - {self.date}"
        
    class Meta:
        ordering = ['-date', '-created_at']

import uuid

from django.db import models

# Create your models here.

class UserRegister(models.Model):

    ROLE_CHOICES = (
        ('photographer', 'Photographer'),
        ('client', 'Client'),
        ('freelance', 'Freelance'),
    )

    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=255)

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='client'
    )

    address = models.TextField(null=True, blank=True)
    place = models.CharField(max_length=100, null=True, blank=True)
    profile_pic = models.ImageField(
        upload_to='profile_pic/',
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name    
    
from django.db import models
from django.utils import timezone
from datetime import timedelta

class PasswordResetOTP(models.Model):

    user = models.ForeignKey(
        UserRegister,
        on_delete=models.CASCADE
    )

    otp = models.CharField(
        max_length=6
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def is_valid(self):
        return timezone.now() <= (
            self.created_at + timedelta(minutes=5)
        )

    def __str__(self):
        return self.user.email

class PhotoFolder(models.Model):
    folder_id = models.CharField(max_length=100)
    password = models.CharField(max_length=100,unique=True)
    created_by = models.ForeignKey(
        UserRegister,
        on_delete=models.CASCADE,
        related_name='folders'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.folder_id
    
class FolderPhoto(models.Model):

    folder = models.ForeignKey(
        PhotoFolder,
        on_delete=models.CASCADE,
        related_name='photos'
    )

    image = models.ImageField(
        upload_to='folder_photos/'
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.folder.folder_id


class PhotoLike(models.Model):

    photo = models.ForeignKey(
        FolderPhoto,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        UserRegister,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = ['photo', 'user']


import uuid

class Album(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    folder = models.ForeignKey(
        PhotoFolder,
        on_delete=models.CASCADE
    )

    created_by = models.ForeignKey(
        UserRegister,
        on_delete=models.CASCADE
    )

    total_pages = models.PositiveIntegerField(default=1)

    photos_per_page = models.JSONField(default=dict)

    photo_ids = models.TextField()

    share_token = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title
    
    
class AlbumPage(models.Model):

    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name='pages'
    )

    page_number = models.IntegerField()

    collage = models.ImageField(
        upload_to='album_pages/'
    )

    def __str__(self):
        return f"{self.album.title} - Page {self.page_number}"

class AlbumPhoto(models.Model):

    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name='album_photos'
    )

    photo = models.ForeignKey(
        FolderPhoto,
        on_delete=models.CASCADE
    )

    page_number = models.IntegerField()

    position = models.IntegerField(
        default=0
    )

    rotation = models.IntegerField(
        default=0
    )

    crop_x = models.FloatField(
        default=0
    )

    crop_y = models.FloatField(
        default=0
    )

    crop_width = models.FloatField(
        default=0
    )

    crop_height = models.FloatField(
        default=0
    )

    edited_image = models.ImageField(
        upload_to='album_edited/',
        null=True,
        blank=True
    )



    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = [
            'page_number',
            'position'
        ]

    def __str__(self):

        return (
            f"{self.album.title}"
            f" - Page {self.page_number}"
            f" - Position {self.position}"
        )
    



#Freelancer
class FreelancerPhotoFolder(models.Model):
    folder_id = models.CharField(max_length=100)
    password = models.CharField(max_length=100,unique=True)
    created_by = models.ForeignKey(
        UserRegister,
        on_delete=models.CASCADE,
        related_name='freelancer_folders'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.folder_id
    

class FreelancerFolderPhoto(models.Model):

    folder = models.ForeignKey(
        FreelancerPhotoFolder,
        on_delete=models.CASCADE,
        related_name='freelancephotos'
    )

    image = models.ImageField(
        upload_to='freelance_folder_photos/'
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.folder.folder_id

class FreelancerAlbum(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    folder = models.ForeignKey(
        FreelancerPhotoFolder,
        on_delete=models.CASCADE
    )

    created_by = models.ForeignKey(
        UserRegister,
        on_delete=models.CASCADE
    )

    total_pages = models.PositiveIntegerField(default=1)

    photos_per_page = models.JSONField(default=dict)

    photo_ids = models.TextField()

    share_token = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title
class FreelancerAlbumPhoto(models.Model):
    
    album = models.ForeignKey(
        FreelancerAlbum,
        on_delete=models.CASCADE,
        related_name='freelance_album_photos'
    )

    photo = models.ForeignKey(
        FreelancerFolderPhoto,
        on_delete=models.CASCADE
    )

    page_number = models.IntegerField()

    position = models.IntegerField(
        default=0
    )

    rotation = models.IntegerField(
        default=0
    )

    crop_x = models.FloatField(
        default=0
    )

    crop_y = models.FloatField(
        default=0
    )

    crop_width = models.FloatField(
        default=0
    )

    crop_height = models.FloatField(
        default=0
    )

    edited_image = models.ImageField(
        upload_to='freelance_album_edited/',
        null=True,
        blank=True
    )



    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = [
            'page_number',
            'position'
        ]

    def __str__(self):

        return (
            f"{self.album.title}"
            f" - Page {self.page_number}"
            f" - Position {self.position}"
        )
    
class FreelancerAlbumPage(models.Model):

    album = models.ForeignKey(
        FreelancerAlbum,
        on_delete=models.CASCADE,
        related_name='pages'
    )

    page_number = models.IntegerField()

    collage = models.ImageField(
        upload_to='freelance_album_pages/'
    )

    def __str__(self):
        return f"{self.album.title} - Page {self.page_number}"
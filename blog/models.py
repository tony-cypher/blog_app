from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    CATEGORY = [
        ('business', 'BUSINESS'),
        ('culture', 'CULTURE'),
        ('celebrity', 'CELEBRITY'),
        ('design', 'DESIGN'),
        ('food', 'FOOD'),
        ('lifestyle', 'LIFESTYLE'),
        ('politics', 'POLITICS'),
        ('sports', 'SPORTS'),
        ('startups', 'STARTUPS'),
        ('tech', 'TECH'),
        ('travel', 'TRAVEL'),
    ]
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    slug = models.SlugField(allow_unicode=True, unique=True)
    category = models.CharField(max_length=20, choices=CATEGORY)
    img = models.ImageField(upload_to='images/', null=True)
    created = models.DateTimeField(default=timezone.now)
    published = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        print(self.title)
        print(self.img)
        super().save(*args, **kwargs)

    def publish(self):
        self.published = timezone.now()
        self.save()
    
    def approve_comment(self):
        return self.comments.filter(approved_comment=True)
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=50)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve_comment(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class Team(models.Model):
    TEAM_CHOICES = [
        ('ceo', 'FOUNDER & CEO'),
        ('vp', 'FOUNDER, VP'),
        ('editor', 'EDITOR STAFF'),
    ]

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    category = models.CharField(max_length=20, choices=TEAM_CHOICES)
    description = models.TextField()
    pics = models.ImageField(upload_to='team/')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return self.email
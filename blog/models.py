from django.db import models
from django.urls import reverse #used to generate URLs by reverting the URL pattern
import uuid                     # Required for unique blog instances


# Create your models here.

class Tag(models.Model):
    """Model representing a blog tags."""
    name = models.CharField(max_length=200, help_text='Enter a blog tag (e.g. sceice)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Blog(models.Model):
    """Model representing an article """
    title = models.CharField(max_length=200)
    blogger = models.ForeignKey('Blogger', on_delete=models.SET_NULL, null=True)
    content = models.TextField(max_length=3000, help_text='Enter main content here')
    create_date = models.DateField(null=True, blank=True)
    tag = models.ManyToManyField('Tag', help_text = 'Select a tag for the blog')
    # Create media 
    #cover = models.ImageField(upload_to='images/')

    class Meta:
        ordering = ['create_date']

    def __str__(self):
        """ String for representing the Model object"""
        #return f'{self.id} {self.title}'
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book"""
#        return reverse('blog-detail', args=[str(self.id)])
        return reverse('blog-detail', kwargs={'pk': self.pk})

    def display_tag(self):
        """ Create a string for the Tag. This is required to display tag in Admin."""
        return ', '.join(genre.name for tag in self.tag.all()[:3])
    display_tag.short_description = 'Tag'

    @property
    def num_of_comments(self):
        return BlogComment.objects.filter(blog_connected=self).count()

#class BlogInstance(models.Model):
#    """Model representing a specific id for an article"""
#    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular blog')
#    blog = models.ForeignKey('Blog', on_delete=models.SET_NULL, null=True)
#    def __str__(self):
#        """String for representing the Model object."""
#        return f'{self.uid} ({self.blog.title})'

class Blogger(models.Model):
    """Model representing an author"""
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['name']
  
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('blogger-detail', kwargs={'pk':self.pk})

    def __str__(self):
        """ String for representing the Model object."""
        return self.name



# -----------   Comment model -------------
# Idea from : https://dev.to/radualexandrub/how-to-create-a-comment-section-for-your-django-blog-3egp

from django.utils import timezone
from django.contrib.auth.models import User

class BlogComment(models.Model):
    blog_connected = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name='comments')
    author= models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)
    comment = models.TextField()

#    def approve(self):
#        self.approved_comment = True
#        self.save()

    def __str__(self):
        return self.text

#    def get_absolute_url(self):
#        return reverse('blog-detail', kwargs={'pk':self.pk})


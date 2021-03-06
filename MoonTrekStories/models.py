from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField

class MoonTrekStories(models.Model):
    title = models.CharField(max_length = 255)
    image = models.ImageField(default = 'placeholder.jpg',
        upload_to = 'storyIMG')
    series = models.IntegerField()
    position = models.IntegerField()
    summary = HTMLField()
    description = models.CharField(max_length = 255, default = "Please replace me.")
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('storyPage', kwargs={'slug': self.slug})

class MoonTrekChapters(models.Model):
    chapter_number = models.IntegerField()
    title = models.CharField(max_length = 255)
    content = HTMLField()
    epilogue = models.BooleanField(default = False)
    slug = models.SlugField()
    story = models.ForeignKey(MoonTrekStories, 
        related_name = 'chapters', 
        on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.story.title} : Chapter {self.chapter_number} - {self.title}"

    def get_absolute_url(self):
        return reverse('chapterPage', kwargs={'slug': self.slug, 'story_slug': self.story.slug})
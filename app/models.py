from django.db import models


class Profile(models.Model):
    title = models.CharField('Title', max_length=100, null=True, blank=True)
    subtitle = models.CharField(
        'Subtitle', max_length=100, null=True, blank=True)
    name = models.CharField('Name', max_length=100)
    job = models.TextField('Work')
    introduction = models.TextField('Introduction')
    github = models.CharField(
        'Github', max_length=100, null=True, blank=True)
    twitter = models.CharField(
        'Twitter', max_length=100, null=True, blank=True)
    linkedin = models.CharField(
        'Linkedin', max_length=100, null=True, blank=True)
    facebook = models.CharField(
        'Facebook', max_length=100, null=True, blank=True)
    instagram = models.CharField(
        'Instagram', max_length=100, null=True, blank=True)
    topimage = models.ImageField(
        upload_to='images', verbose_name='TopFigure')
    subimage = models.ImageField(
        upload_to='images', verbose_name='SubFigure')

    def __str__(self):
        return self.name


class Work(models.Model):
    title = models.CharField('Title', max_length=100)
    image = models.ImageField(upload_to='images', verbose_name='Image')
    thumbnail = models.ImageField(
        upload_to='images', verbose_name='Thumnail', null=True, blank=True)
    skill = models.CharField('Skill', max_length=100)
    url = models.CharField('URL', max_length=100, null=True, blank=True)
    created = models.DateField('Date')
    description = models.TextField('Description')


def __str__(self):
    return self.title

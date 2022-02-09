from django.db import models


class Usertest(models.Model):
    title = models.CharField('Name', max_length=200)
    task = models.TextField('Description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Test Case'
        verbose_name_plural = 'Test Cases'

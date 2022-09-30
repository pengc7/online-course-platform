from django.db import models

# Create your models here.
class Course(models.Model):
    image = models.ImageField(upload_to='images/') #create images/ dir to store images
    summary = models.CharField(max_length=200)

    def __str__(self):#so on admin page, the course summary will show for each entry
        return self.summary

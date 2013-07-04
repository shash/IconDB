from django.db import models

class IconImage(models.Model):
    image = models.ImageField(upload_to='icons')
    caption = models.CharField(max_length=45)
    source = models.CharField(max_length=100)
    

class Icon(models.Model):
    photos = models.ManyToManyField('IconImage')
    style = models.CharField(max_length=45)
    century = models.IntegerField()
    location = models.CharField(max_length=45)
    innovations = models.TextField()
    notes = models.TextField()
    element = models.ForeignKey('Element')
    iconType = models.ForeignKey('IconType')
    locationMaster = models.ForeignKey('LocationMaster')
    iconStyle = models.ForeignKey('IconStyle')

class Element(models.Model):
    name = models.CharField(max_length=45)
    purana = models.TextField()
    iconography = models.TextField()

class IconType(models.Model):
    description = models.TextField()

class IconStyle(models.Model):
    description = models.TextField()

class LocationMaster(models.Model):
    correctName = models.CharField(max_length=45)
    sungBy = models.CharField(max_length=45)
    history = models.TextField()
    commonName  = models.CharField(max_length=45)



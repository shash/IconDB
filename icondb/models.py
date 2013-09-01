from django.db import models

class IconImage(models.Model):
    image = models.FileField(upload_to='icons')
    caption = models.CharField(max_length=45)
    source = models.CharField(max_length=100)
    def __str__(self):
	    return self.caption
    

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
    def __str__(self):
	    return self.location + ' ' + self.iconType.name

class Element(models.Model):
    name = models.CharField(max_length=45)
    purana = models.TextField()
    iconography = models.TextField()
    def __str__(self):
	    return self.name

class IconType(models.Model):
    description = models.TextField()
    name = models.CharField(max_length=45)
    def __repr__(self):
	    return self.description

class IconStyle(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()
    def __repr__(self):
	    return self.description

class LocationMaster(models.Model):
    correctName = models.CharField(max_length=45)
    sungBy = models.CharField(max_length=45)
    history = models.TextField()
    commonName  = models.CharField(max_length=45)
    def __repr__(self):
	    return (self.commonName, self.correctName, self.sungBy)
    def __str__(self):
	    return str(self.commonName)



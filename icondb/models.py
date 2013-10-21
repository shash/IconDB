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
    innovations = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    element = models.ForeignKey('Element')
    iconType = models.ForeignKey('IconType')
    site = models.ForeignKey('Site')
    iconStyle = models.ForeignKey('IconStyle')
    def __str__(self):
	    return str(self.site) + ' ' + self.iconType.name

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

class Site(models.Model):
    TEMPLE = 'TEMPLE'
    MUSEUM = 'MUSEUM'
    SITE_TYPES = (
        (TEMPLE, 'Temple'),
        (MUSEUM, 'Museum'),
    )
    correctName = models.CharField(max_length=45)
    siteType = models.CharField(max_length=45, choices=SITE_TYPES, default=TEMPLE)
    sungBy = models.CharField(max_length=45)
    history = models.TextField()
    commonName  = models.CharField(max_length=45)
    dynasty = models.CharField(max_length=45)
    location = models.ForeignKey('Location')
    def __repr__(self):
	    return (self.commonName, self.correctName, self.sungBy)
    def __str__(self):
	    return str(self.commonName)

class Location(models.Model):
    name = models.CharField(max_length=45)
    old_name = models.CharField(max_length=45)
    description = models.TextField()
    state = models.CharField(max_length=45)
    district = models.CharField(max_length=45)
    taluk = models.CharField(max_length =45)
    directions = models.TextField()
    coordinates = models.CharField(max_length=45)
    
    def __str__(self):
        return self.name


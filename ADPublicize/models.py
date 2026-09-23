from django.db import models


class advertiser(models.Model):
    adverid = models.AutoField(verbose_name='ADVERID', serialize=False, auto_created=True, primary_key=True)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    role = models.CharField(max_length=25)
    emailid = models.EmailField(max_length=50)
    password = models.CharField(max_length=25)

    class Meta:
        db_table = "advertisertbl"


class publiser(models.Model):
    pubid = models.AutoField(verbose_name='PUBID', serialize=False, auto_created=True, primary_key=True)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    cname = models.CharField(max_length=50)
    addres1 = models.CharField(max_length=100)
    addres2 = models.CharField(max_length=100)
    emailid = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    password = models.CharField(max_length=25)

    class Meta:
        db_table = "publisertbl"


class contactus(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    emailid = models.CharField(max_length=50)
    monumber = models.BigIntegerField
    message = models.CharField(max_length=10000)

    class Meta:
        db_table = "contactustbl"


class SavLoc(models.Model):
    locid = models.AutoField(verbose_name='LOCID', serialize=False, auto_created=True, primary_key=True)
    pubid = models.IntegerField()
    locimage = models.FileField()
    locname = models.CharField(max_length=100)
    locaddress = models.CharField(max_length=150)
    pcname = models.CharField(max_length=50)
    contactno = models.BigIntegerField()
    parea = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    ADVERTISE_TYPE = (
        ('Banner', 'Banner'),
        ('Bus Stand', 'Bus Stand'),
        ('Electric Poll', 'Electric Poll')
    )
    adtype = models.CharField(max_length=20, choices=ADVERTISE_TYPE)
    noadv = models.IntegerField()
    advsize = models.CharField(max_length=25)
    advprice = models.IntegerField()

    class Meta:
        db_table = "addloctiontbl"


class advRequest(models.Model):
    advrequestid = models.AutoField(verbose_name='ADVREQUESTID', serialize=False, auto_created=True, primary_key=True)
    locaddress = models.CharField(max_length=500)
    parea = models.CharField(max_length= 100)
    city = models.CharField(max_length= 100)
    adtype = models.CharField(max_length=100)
    advsize = models.CharField(max_length=50)
    advprice = models.IntegerField()
    pubid = models.IntegerField()
    locid = models.IntegerField()
    adverid = models.IntegerField()
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    cname = models.CharField(max_length=500)
    contactno = models.BigIntegerField()
    starttime = models.DateField()
    lastdate = models.DateField()

    class Meta:
        db_table = "advrequesttbl"
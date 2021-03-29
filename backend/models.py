from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=25)
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, default="")
    address1 = models.TextField()
    address2 = models.TextField()
    city = models.CharField(max_length=75)
    state = models.CharField(max_length=2)
    zipcode = models.IntegerField()
    employername = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class SubscriptionType(models.Model):
    subscriptiontypecode = models.IntegerField()
    subscriptiontypename = models.CharField(max_length=50)

    def __str__(self):
        return self.subscriptiontypename


class Service(models.Model):
    servicecode = models.IntegerField()
    servicename = models.CharField(max_length=50)
    description = models.TextField()
    premium = models.BooleanField()
    allocation = models.CharField(max_length=50)

    def __str__(self):
        return self.servicecode


class Office(models.Model):
    officecode = models.IntegerField()
    officename = models.CharField(max_length=50)
    attribution = models.TextField()

    def __str__(self):
        return self.officecode


class Organization(models.Model):
    organizationcode = models.IntegerField()
    description = models.TextField()
    datejoined = models.DateField()
    address1 = models.TextField()
    address2 = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zipcode = models.IntegerField()
    phonenumber = models.TextField()

    def __str__(self):
        return self.organizationcode


class Subscriber(models.Model):
    subscriberID = models.IntegerField()
    username = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    subscriptiontypecode = models.ForeignKey(SubscriptionType, on_delete=models.CASCADE)
    servicecode = models.ForeignKey(Service, on_delete=models.CASCADE)
    requestdate = models.DateField()
    startdate = models.DateField()
    enddate = models.DateField()
    motifofcancellation = models.TextField()

    def __str__(self):
        return self.subscriberID


class TransferredSubscription(models.Model):
    transferID = models.IntegerField()
    transferfrom = models.TextField()
    transferto = models.TextField()
    requestdate = models.DateField()
    transferdate = models.DateField()
    subscriberID = models.ForeignKey(Subscriber, on_delete=models.CASCADE)

    def __str__(self):
        return self.transferID


class Officer(models.Model):
    officecode = models.ForeignKey(Office, on_delete=models.CASCADE)
    subscriberID = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    startdate = models.DateField()
    enddate = models.DateField()


    def __str__(self):
        return self.officecode


class OrganizationMember(models.Model):
    organizationcode = models.ForeignKey(Organization, on_delete=models.CASCADE)
    subscriberID = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    startdate = models.DateField()
    enddate = models.DateField()
    nativecountry = models.CharField(max_length=50)
    citizenship = models.CharField(max_length=50)
    isdelegate = models.BooleanField()
from django.contrib.auth import get_user_model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()


class Company(models.Model):
    name = models.CharField(verbose_name='name', max_length=200, unique=True)
    address = models.TextField()
    discription = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='company_creator')
    moderator = models.ManyToManyField(User, blank=True,
                                       related_name='company_moder')

    class Meta:
        ordering = ['name']


class Employee(models.Model):
    lastname = models.CharField(verbose_name='lastname', max_length=100)
    firstname = models.CharField(verbose_name='firstname', max_length=100)
    secondname = models.CharField(verbose_name='secondname', max_length=100)
    position = models.TextField()
    phone_number = PhoneNumberField(blank=True)
    office_number = PhoneNumberField(blank=True)
    fax_number = PhoneNumberField(blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                related_name='employee')

    class Meta:
        unique_together = ('lastname', 'firstname', 'secondname', 'company')

    def __str__(self):
        return '%s %s %s (%s)' % (self.lastname,
                                  self.firstname,
                                  self.secondname,
                                  self.position)

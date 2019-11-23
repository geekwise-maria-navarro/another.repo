from django.db import models

# Create your models here.

class Branch(models.Model):
    bank_name = models.CharField(max_length=200)
    bank_location = models.CharField(max_length=200)

    def __str__(self):
        return (f"Bank name: {self.bank_name}")

class Customer(models.Model):
    branch = models.ForeignKey(
        Branch,
        on_delete = models.CASCADE
    )
    
    customer_first_name = models.CharField(max_length=200)
    customer_last_name = models.CharField(max_length=200)
    customer_email = models.EmailField(max_length=250)

    def __str__(self):
        return (f"Customer Name: {self.customer_first_name} {self.customer_last_name} | Bank: {self.branch.bank_name}")

class Product(models.Model):
    prodcut_options = (
        ('checking', 'CHECKING'),
        ('savings', 'SAVINGS'),
        ('debit', 'DEBIT'),
        ('credit', 'CREDIT'),
    )

    prodcut_options = models.CharField(
        max_length=200,
        choices = prodcut_options,
        default = prodcut_options[0]
    )
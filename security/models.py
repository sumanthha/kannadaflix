import datetime
from google.appengine.ext import db
from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin
class Account(models.Model):
    user  = models.ForeignKey(User)
    pannumber = models.CharField(max_length=100)
    addressa  = models.CharField(max_length=800)
    addressb  = models.CharField(max_length=800)
    city      = models.CharField(max_length=100)
    state     = models.CharField(max_length=100)
    zipcode   = models.CharField(max_length=40)
    homephone = models.CharField(max_length=40)
    mobilephone = models.CharField(max_length=40)
    joindate    = models.DateField(auto_now_add=True)
    totalvalue = models.FloatField( default = 0.)
    moneyremainig   = models.FloatField( default=0.)
    moneyinvested = models.FloatField(default=0.)
    
    class Meta:
        db_table = 'Account'
        
class AccountAdmin(admin.ModelAdmin):
    pass
admin.site.register(Account, AccountAdmin)
            
class BankAccount(models.Model):
    
    user       = models.ForeignKey(User)
    bankname      = models.CharField(max_length=400)
    nickname  	  = models.CharField(max_length=400)
    accountnumber = models.CharField(max_length=400)
    routingnumber = models.CharField(max_length=400)
    bankaddress   = models.CharField(max_length=800)
    bankaddressb  = models.CharField(max_length=800)
    class Meta:
	    db_table = 'BankAccount'
	    
class BankAccountAdmin(admin.ModelAdmin):
    pass
admin.site.register(BankAccount, BankAccountAdmin)

class AccountTransations(models.Model):
    account = models.ForeignKey( Account)
    bank    = models.ForeignKey( BankAccount)
    
    transation_type = models.CharField(max_length=1,
                         choices=( ( 'D' , 'Deposit' ),( 'W' , 'Withdraw') ) )
                         
    amount  = models.FloatField()
    transacation_date = models.DateField(auto_now_add=True)
    sucess = models.BooleanField()
    notes  = models.CharField(max_length=4000)
    class Meta:
        db_table = 'AccountTransations'
        
class AccountTransationsAdmin(admin.ModelAdmin):
    pass
admin.site.register(AccountTransations, AccountTransationsAdmin)
    
import datetime
from google.appengine.ext import db
from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin

class Loan(models.Model):
    APPLIED = 'A'
    FUNDED  = 'F'
    FUNDING_IN_PROCESS = 'FIP'
     
    LOAN_STATES = ( ( APPLIED,'Applied' ),
                           ( FUNDED , 'Funded' ),
                           ( FUNDING_IN_PROCESS , 'Funding in Process' ) ,
                           )
                           
    
    borrower = models.ForeignKey(User)
    loan_amount = models.FloatField()
    applydate   = models.DateField(auto_now_add=True)
    is_approved = models.BooleanField()
    loan_yield  = models.FloatField()
    approvedate = models.DateField()
    nextpaydate = models.DateField()
    class Meta:
        db_table = 'Loan'         

	    
class LoanAdmin(admin.ModelAdmin):
    pass
admin.site.register(Loan, LoanAdmin)

class InvestorLoanMap(models.Model):
    
    invester = models.ForeignKey(User)
    amount_invested = models.FloatField()
    loan     = models.ForeignKey(Loan)
    class Meta:
        db_table = 'InvestorLoanMap'
        
class InvestorLoanMapAdmin(admin.ModelAdmin):
    pass
admin.site.register(InvestorLoanMap, InvestorLoanMapAdmin)

'''
Payments may by the loaner
'''
class BorrowerPayments( models.Model):
    
    paydate  = models.DateField(auto_now_add=True)   
    princpay = models.FloatField()
    intpay   = models.FloatField()
    loan_remaining = models.FloatField()
    borrower   = models.ForeignKey(User)
    loan       = models.ForeignKey(Loan)
    class Meta:
        db_table = 'BorrowerPayments'

class BorrowerPaymentsAdmin(admin.ModelAdmin):
    pass
admin.site.register(BorrowerPayments, BorrowerPaymentsAdmin)

class InvestorPayemnts(models.Model):       
    
    paydate  = models.DateField(auto_now_add=True)
    princpay = models.FloatField()
    intpay  = models.FloatField()
    investor = models.ForeignKey(User)
    class Meta:
        db_table = 'InvestorPayement'
           
class InvestorPayemntsAdmin(admin.ModelAdmin):
    pass
admin.site.register(InvestorPayemnts, InvestorPayemntsAdmin)


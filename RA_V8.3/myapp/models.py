from django.db import models

from django import forms

#Activeuser table
class activeusers(models.Model):
    id = models.IntegerField(primary_key=True,null=False,default=False)
    OrganizationName = models.CharField(max_length=45)
    FullName = models.CharField(max_length=200)
    EmailAddress =  models.CharField(max_length=100)
    Name = models.CharField(null=False,max_length=60)
    PostalAddress = models.CharField(max_length=150)
    UserCreationDate =  models.CharField(null=False,max_length=50)
    LastLoginDate = models.CharField(max_length=50)
    LoginStatus = models.CharField(max_length=50)
    PreferredFileServer = models.CharField(max_length=30)
    AuditGroup = models.CharField(max_length=30)
    GenericGroup =  models.CharField(max_length=15)
    UserLastModificationDate = models.CharField(max_length=30)
    ReportWeek = models.IntegerField(null=False)
    ReportYear = models.IntegerField(null=False)
    class Meta:
        # managed = False
        db_table = 'activeusers' # your view name
        unique_together = (('id','Name', 'ReportWeek','ReportYear','UserCreationDate'),)


#Loggedinusers Table
class loggedinusers(models.Model):
    id = models.IntegerField(primary_key=True,null=False,default=False)
    EventLabel = models.CharField(max_length=45)
    EventKey = models.CharField(max_length=50)
    EventTime = models.CharField(null=False,max_length=50)
    UserName = models.CharField(max_length=100)
    UserID = models.CharField(null=False,max_length=60)
    IPAddress = models.CharField(max_length=50)
    UserOrganization = models.CharField(max_length=20)
    ObjectType = models.CharField(max_length=50)
    ObjectID = models.CharField(max_length=50)
    ObjectType_Branch_ID = models.CharField(max_length=50)
    ObjectName = models.CharField(max_length=50)
    ObjectNumber = models.CharField(max_length=50)
    BranchID= models.CharField(max_length=50)
    WorkingBranchID = models.CharField(max_length=50)
    Version = models.CharField(max_length=50)
    MasterID = models.CharField(max_length=50)
    OrganizationID = models.CharField(max_length=50)
    OrganizationName=models.CharField(max_length=50)
    ContextID = models.CharField(max_length=50)
    ContextName = models.CharField(max_length=50)
    ContextType_Branch_ID = models.CharField(max_length=50)
    FolderPath = models.CharField(max_length=50)
    DomainPath = models.CharField(max_length=50)
    Identity = models.CharField(max_length=50)
    LifecycleState =models.CharField(max_length=45)
    TransactionDescription = models.CharField(max_length=50)
    ObjectIdentity = models.CharField(max_length=50)
    SecurityLabels = models.CharField(max_length=50)
    EventSpecificData =models.CharField(max_length=50)
    ReportWeek = models.IntegerField(null=False)
    ReportYear = models.IntegerField(null=False)
    class Meta:
        managed = False
        db_table = 'loggedinusers' # your view name
        unique_together = (('id','EventTime', 'ReportWeek','ReportYear','UserID'),)

class organization(models.Model):
    sno=models.IntegerField(primary_key=True,null=False,default=False)
    org=models.CharField(max_length=45)
    class Meta:
        db_table = 'organization'
        

#Views for Active users
class active_braking(models.Model):
    id = models.IntegerField(primary_key=True,null=False,default=False)
    OrganizationName = models.CharField(max_length=45)
    FullName = models.CharField(max_length=200)
    EmailAddress =  models.CharField(max_length=100)
    Name = models.CharField(null=False,max_length=60)
    PostalAddress = models.CharField(max_length=150)
    UserCreationDate =  models.CharField(null=False,max_length=50)
    LastLoginDate = models.CharField(max_length=50)
    LoginStatus = models.CharField(max_length=50)
    PreferredFileServer = models.CharField(max_length=30)
    AuditGroup = models.CharField(max_length=30)
    GenericGroup =  models.CharField(max_length=15)
    UserLastModificationDate = models.CharField(max_length=30)
    ReportWeek = models.IntegerField(null=False)
    ReportYear = models.IntegerField(null=False)
    class Meta:
        # managed = False
        db_table = 'active_braking' # your view name
        unique_together = (('id','Name', 'ReportWeek','ReportYear','UserCreationDate'),)

class active_elec(models.Model):
    id = models.IntegerField(primary_key=True,null=False,default=False)
    OrganizationName = models.CharField(max_length=45)
    FullName = models.CharField(max_length=200)
    EmailAddress =  models.CharField(max_length=100)
    Name = models.CharField(null=False,max_length=60)
    PostalAddress = models.CharField(max_length=150)
    UserCreationDate =  models.CharField(null=False,max_length=50)
    LastLoginDate = models.CharField(max_length=50)
    LoginStatus = models.CharField(max_length=50)
    PreferredFileServer = models.CharField(max_length=30)
    AuditGroup = models.CharField(max_length=30)
    GenericGroup =  models.CharField(max_length=15)
    UserLastModificationDate = models.CharField(max_length=30)
    ReportWeek = models.IntegerField(null=False)
    ReportYear = models.IntegerField(null=False)
    class Meta:
        # managed = False
        db_table = 'active_elec' # your view name
        unique_together = (('id','Name', 'ReportWeek','ReportYear','UserCreationDate'),)

class active_css(models.Model):
    id = models.IntegerField(primary_key=True,null=False,default=False)
    OrganizationName = models.CharField(max_length=45)
    FullName = models.CharField(max_length=200)
    EmailAddress =  models.CharField(max_length=100)
    Name = models.CharField(null=False,max_length=60)
    PostalAddress = models.CharField(max_length=150)
    UserCreationDate =  models.CharField(null=False,max_length=50)
    LastLoginDate = models.CharField(max_length=50)
    LoginStatus = models.CharField(max_length=50)
    PreferredFileServer = models.CharField(max_length=30)
    AuditGroup = models.CharField(max_length=30)
    GenericGroup =  models.CharField(max_length=15)
    UserLastModificationDate = models.CharField(max_length=30)
    ReportWeek = models.IntegerField(null=False)
    ReportYear = models.IntegerField(null=False)
    class Meta:
        # managed = False
        db_table = 'active_css' # your view name
        unique_together = (('id','Name', 'ReportWeek','ReportYear','UserCreationDate'),)

class active_oss(models.Model):
    id = models.IntegerField(primary_key=True,null=False,default=False)
    OrganizationName = models.CharField(max_length=45)
    FullName = models.CharField(max_length=200)
    EmailAddress =  models.CharField(max_length=100)
    Name = models.CharField(null=False,max_length=60)
    PostalAddress = models.CharField(max_length=150)
    UserCreationDate =  models.CharField(null=False,max_length=50)
    LastLoginDate = models.CharField(max_length=50)
    LoginStatus = models.CharField(max_length=50)
    PreferredFileServer = models.CharField(max_length=30)
    AuditGroup = models.CharField(max_length=30)
    GenericGroup =  models.CharField(max_length=15)
    UserLastModificationDate = models.CharField(max_length=30)
    ReportWeek = models.IntegerField(null=False)
    ReportYear = models.IntegerField(null=False)
    class Meta:
        # managed = False
        db_table = 'active_oss' # your view name
        unique_together = (('id','Name', 'ReportWeek','ReportYear','UserCreationDate'),)

class active_lvs(models.Model):
    id = models.IntegerField(primary_key=True,null=False,default=False)
    OrganizationName = models.CharField(max_length=45)
    FullName = models.CharField(max_length=200)
    EmailAddress =  models.CharField(max_length=100)
    Name = models.CharField(null=False,max_length=60)
    PostalAddress = models.CharField(max_length=150)
    UserCreationDate =  models.CharField(null=False,max_length=50)
    LastLoginDate = models.CharField(max_length=50)
    LoginStatus = models.CharField(max_length=50)
    PreferredFileServer = models.CharField(max_length=30)
    AuditGroup = models.CharField(max_length=30)
    GenericGroup =  models.CharField(max_length=15)
    UserLastModificationDate = models.CharField(max_length=30)
    ReportWeek = models.IntegerField(null=False)
    ReportYear = models.IntegerField(null=False)
    class Meta:
        # managed = False
        db_table = 'active_lvs' # your view name
        unique_together = (('id','Name', 'ReportWeek','ReportYear','UserCreationDate'),)



#Views for Loggedin users

class loggedin_braking(models.Model):
    id = models.IntegerField(primary_key=True,null=False,default=False)
    EventLabel = models.CharField(max_length=45)
    EventKey = models.CharField(max_length=50)
    EventTime = models.CharField(null=False,max_length=50)
    UserName = models.CharField(max_length=100)
    UserID = models.CharField(null=False,max_length=60)
    IPAddress = models.CharField(max_length=50)
    UserOrganization = models.CharField(max_length=20)
    ObjectType = models.CharField(max_length=50)
    ObjectID = models.CharField(max_length=50)
    ObjectType_Branch_ID = models.CharField(max_length=50)
    ObjectName = models.CharField(max_length=50)
    ObjectNumber = models.CharField(max_length=50)
    BranchID= models.CharField(max_length=50)
    WorkingBranchID = models.CharField(max_length=50)
    Version = models.CharField(max_length=50)
    MasterID = models.CharField(max_length=50)
    OrganizationID = models.CharField(max_length=50)
    OrganizationName=models.CharField(max_length=50)
    ContextID = models.CharField(max_length=50)
    ContextName = models.CharField(max_length=50)
    ContextType_Branch_ID = models.CharField(max_length=50)
    FolderPath = models.CharField(max_length=50)
    DomainPath = models.CharField(max_length=50)
    Identity = models.CharField(max_length=50)
    LifecycleState =models.CharField(max_length=45)
    TransactionDescription = models.CharField(max_length=50)
    ObjectIdentity = models.CharField(max_length=50)
    SecurityLabels = models.CharField(max_length=50)
    EventSpecificData =models.CharField(max_length=50)
    ReportWeek = models.IntegerField(null=False)
    ReportYear = models.IntegerField(null=False)
    class Meta:
        managed = False
        db_table = 'loggedin_braking' # your view name
        unique_together = (('id','EventTime', 'ReportWeek','ReportYear','UserID'),)

class loggedin_Elec(models.Model):
    id = models.IntegerField(primary_key=True,null=False,default=False)
    EventLabel = models.CharField(max_length=45)
    EventKey = models.CharField(max_length=50)
    EventTime = models.CharField(null=False,max_length=50)
    UserName = models.CharField(max_length=100)
    UserID = models.CharField(null=False,max_length=60)
    IPAddress = models.CharField(max_length=50)
    UserOrganization = models.CharField(max_length=20)
    ObjectType = models.CharField(max_length=50)
    ObjectID = models.CharField(max_length=50)
    ObjectType_Branch_ID = models.CharField(max_length=50)
    ObjectName = models.CharField(max_length=50)
    ObjectNumber = models.CharField(max_length=50)
    BranchID= models.CharField(max_length=50)
    WorkingBranchID = models.CharField(max_length=50)
    Version = models.CharField(max_length=50)
    MasterID = models.CharField(max_length=50)
    OrganizationID = models.CharField(max_length=50)
    OrganizationName=models.CharField(max_length=50)
    ContextID = models.CharField(max_length=50)
    ContextName = models.CharField(max_length=50)
    ContextType_Branch_ID = models.CharField(max_length=50)
    FolderPath = models.CharField(max_length=50)
    DomainPath = models.CharField(max_length=50)
    Identity = models.CharField(max_length=50)
    LifecycleState =models.CharField(max_length=45)
    TransactionDescription = models.CharField(max_length=50)
    ObjectIdentity = models.CharField(max_length=50)
    SecurityLabels = models.CharField(max_length=50)
    EventSpecificData =models.CharField(max_length=50)
    ReportWeek = models.IntegerField(null=False)
    ReportYear = models.IntegerField(null=False)
    class Meta:
        managed = False
        db_table = 'loggedin_Elec' # your view name
        unique_together = (('id','EventTime', 'ReportWeek','ReportYear','UserID'),)

class loggedin_css(models.Model):
    id = models.IntegerField(primary_key=True,null=False,default=False)
    EventLabel = models.CharField(max_length=45)
    EventKey = models.CharField(max_length=50)
    EventTime = models.CharField(null=False,max_length=50)
    UserName = models.CharField(max_length=100)
    UserID = models.CharField(null=False,max_length=60)
    IPAddress = models.CharField(max_length=50)
    UserOrganization = models.CharField(max_length=20)
    ObjectType = models.CharField(max_length=50)
    ObjectID = models.CharField(max_length=50)
    ObjectType_Branch_ID = models.CharField(max_length=50)
    ObjectName = models.CharField(max_length=50)
    ObjectNumber = models.CharField(max_length=50)
    BranchID= models.CharField(max_length=50)
    WorkingBranchID = models.CharField(max_length=50)
    Version = models.CharField(max_length=50)
    MasterID = models.CharField(max_length=50)
    OrganizationID = models.CharField(max_length=50)
    OrganizationName=models.CharField(max_length=50)
    ContextID = models.CharField(max_length=50)
    ContextName = models.CharField(max_length=50)
    ContextType_Branch_ID = models.CharField(max_length=50)
    FolderPath = models.CharField(max_length=50)
    DomainPath = models.CharField(max_length=50)
    Identity = models.CharField(max_length=50)
    LifecycleState =models.CharField(max_length=45)
    TransactionDescription = models.CharField(max_length=50)
    ObjectIdentity = models.CharField(max_length=50)
    SecurityLabels = models.CharField(max_length=50)
    EventSpecificData =models.CharField(max_length=50)
    ReportWeek = models.IntegerField(null=False)
    ReportYear = models.IntegerField(null=False)
    class Meta:
        managed = False
        db_table = 'loggedin_css' # your view name
        unique_together = (('id','EventTime', 'ReportWeek','ReportYear','UserID'),)

class loggedin_oss(models.Model):
    id = models.IntegerField(primary_key=True,null=False,default=False)
    EventLabel = models.CharField(max_length=45)
    EventKey = models.CharField(max_length=50)
    EventTime = models.CharField(null=False,max_length=50)
    UserName = models.CharField(max_length=100)
    UserID = models.CharField(null=False,max_length=60)
    IPAddress = models.CharField(max_length=50)
    UserOrganization = models.CharField(max_length=20)
    ObjectType = models.CharField(max_length=50)
    ObjectID = models.CharField(max_length=50)
    ObjectType_Branch_ID = models.CharField(max_length=50)
    ObjectName = models.CharField(max_length=50)
    ObjectNumber = models.CharField(max_length=50)
    BranchID= models.CharField(max_length=50)
    WorkingBranchID = models.CharField(max_length=50)
    Version = models.CharField(max_length=50)
    MasterID = models.CharField(max_length=50)
    OrganizationID = models.CharField(max_length=50)
    OrganizationName=models.CharField(max_length=50)
    ContextID = models.CharField(max_length=50)
    ContextName = models.CharField(max_length=50)
    ContextType_Branch_ID = models.CharField(max_length=50)
    FolderPath = models.CharField(max_length=50)
    DomainPath = models.CharField(max_length=50)
    Identity = models.CharField(max_length=50)
    LifecycleState =models.CharField(max_length=45)
    TransactionDescription = models.CharField(max_length=50)
    ObjectIdentity = models.CharField(max_length=50)
    SecurityLabels = models.CharField(max_length=50)
    EventSpecificData =models.CharField(max_length=50)
    ReportWeek = models.IntegerField(null=False)
    ReportYear = models.IntegerField(null=False)
    class Meta:
        managed = False
        db_table = 'loggedin_oss' # your view name
        unique_together = (('id','EventTime', 'ReportWeek','ReportYear','UserID'),)

class loggedin_lvs(models.Model):
    id = models.IntegerField(primary_key=True,null=False,default=False)
    EventLabel = models.CharField(max_length=45)
    EventKey = models.CharField(max_length=50)
    EventTime = models.CharField(null=False,max_length=50)
    UserName = models.CharField(max_length=100)
    UserID = models.CharField(null=False,max_length=60)
    IPAddress = models.CharField(max_length=50)
    UserOrganization = models.CharField(max_length=20)
    ObjectType = models.CharField(max_length=50)
    ObjectID = models.CharField(max_length=50)
    ObjectType_Branch_ID = models.CharField(max_length=50)
    ObjectName = models.CharField(max_length=50)
    ObjectNumber = models.CharField(max_length=50)
    BranchID= models.CharField(max_length=50)
    WorkingBranchID = models.CharField(max_length=50)
    Version = models.CharField(max_length=50)
    MasterID = models.CharField(max_length=50)
    OrganizationID = models.CharField(max_length=50)
    OrganizationName=models.CharField(max_length=50)
    ContextID = models.CharField(max_length=50)
    ContextName = models.CharField(max_length=50)
    ContextType_Branch_ID = models.CharField(max_length=50)
    FolderPath = models.CharField(max_length=50)
    DomainPath = models.CharField(max_length=50)
    Identity = models.CharField(max_length=50)
    LifecycleState =models.CharField(max_length=45)
    TransactionDescription = models.CharField(max_length=50)
    ObjectIdentity = models.CharField(max_length=50)
    SecurityLabels = models.CharField(max_length=50)
    EventSpecificData =models.CharField(max_length=50)
    ReportWeek = models.IntegerField(null=False)
    ReportYear = models.IntegerField(null=False)
    class Meta:
        managed = False
        db_table = 'loggedin_lvs' # your view name
        unique_together = (('id','EventTime', 'ReportWeek','ReportYear','UserID'),)

class uploadmodel(models.Model):
    Before = models.FileField(upload_to=None)
    From = models.FileField(upload_to=None)
    AuditReport = models.FileField(upload_to=None)

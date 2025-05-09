# team details
from django.db import models

class Team(models.Model):
    teamId = models.AutoField(primary_key=True)
    teamName = models.CharField(max_length=100)
    teamLead = models.CharField(max_length=100)

    def __str__(self):
        return self.teamName


# teamLEad details

class TeamLead(models.Model):
    teamLeadId = models.AutoField(primary_key=True)
    teamLeadName = models.CharField(max_length=100)

    def __str__(self):
        return self.teamLeadName

# team details
class UserProfile(models.Model):
    teamMemberId = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobileNumber = models.CharField(max_length=15)
    team = models.CharField(max_length=100 , default="not assigned")  # CHANGED from ForeignKey to CharField
    teamLead = models.CharField(max_length=100 ,  default="Not Assigned")  # NEW field
    isActive = models.BooleanField(default=True)
    isActiveRemarks = models.TextField(blank=True, null=True)
    isAccountLocked = models.BooleanField(default=False)
    isAccountLockedRemarks = models.TextField(blank=True, null=True)
    createdBy = models.CharField(max_length=100)

    def __str__(self):
        return self.userName


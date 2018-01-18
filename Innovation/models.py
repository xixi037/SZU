from django.db import models

# Create your models here.
class Managers(models.Model):
    username = models.CharField(primary_key=True, max_length=255)
    password = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'managers'


class Middle(models.Model):
    pro_id = models.IntegerField(blank=True, null=True)
    export_time = models.CharField(max_length=255, blank=True, null=True, default='')
    status = models.CharField(max_length=1, blank=True, null=True, default='')
    leader_id = models.CharField(primary_key=True, max_length=255)
    pro_num = models.CharField(max_length=255, blank=True, null=True, default='')
    pro_mems = models.CharField(max_length=255, blank=True, null=True, default='')
    pro_endtime = models.CharField(max_length=255, blank=True, null=True, default='')
    pro_etime = models.CharField(max_length=255, blank=True, null=True, default='')
    pro_stime = models.CharField(max_length=255, blank=True, null=True, default='')
    pro_schedule = models.TextField(blank=True, null=True, default='')
    pro_source = models.TextField(blank=True, null=True, default='')
    pro_money = models.TextField(blank=True, null=True, default='')
    pro_difficulties = models.TextField(blank=True, null=True, default='')
    pro_advice = models.TextField(blank=True, null=True, default='')
    pro_change = models.TextField(blank=True, null=True, default='')
    pro_plan = models.TextField(blank=True, null=True, default='')
    pro_harvest = models.TextField(blank=True, null=True, default='')

    class Meta:
        managed = False
        db_table = 'middle'


class ProInfo(models.Model):
    pro_name = models.CharField(max_length=255, blank=True, null=True)
    tutor_id = models.CharField(max_length=255, blank=True, null=True)
    leader_id = models.CharField(max_length=255)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pro_info'
        unique_together = (('id', 'leader_id'),)


class Users(models.Model):
    username = models.CharField(primary_key=True, max_length=255)
    password = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    classID = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    major = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True, default='')
    email = models.CharField(max_length=255, blank=True, null=True, default='')

    class Meta:
        managed = False
        db_table = 'users'









from django.db import models

# Create your models here.
class Managers(models.Model):
    username = models.CharField(primary_key=True, max_length=255)
    password = models.CharField(max_length=255, blank=True, null=True)

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
    classID = models.CharField(max_length=255, blank=True, null=True)
    major = models.CharField(max_length=255, blank=True, null=True)
    institute = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True, default='')
    email = models.CharField(max_length=255, blank=True, null=True, default='')

    class Meta:
        managed = False
        db_table = 'users'

class Members(models.Model):
    pro_id = models.IntegerField()
    stu_id = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'members'

class Status(models.Model):
    mode = models.IntegerField()
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'status'


class Conclude(models.Model):
    pro_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=1, blank=True, null=True, default='')
    fillin_time = models.CharField(max_length=255, blank=True, null=True, default='')
    export_time = models.CharField(max_length=255, blank=True, null=True, default='')
    pro_num = models.CharField(max_length=255, blank=True, null=True, default='')
    leader_id = models.CharField(max_length=255, blank=True, null=True)
    pro_time = models.CharField(max_length=255, blank=True, null=True, default='')
    leader_ethnicity = models.CharField(max_length=255, blank=True, null=True, default='')
    leader_birth = models.CharField(max_length=255, blank=True, null=True, default='')
    leader_address = models.CharField(max_length=255, blank=True, null=True, default='')
    leader_institute = models.CharField(max_length=255, blank=True, null=True, default='')
    leader_job = models.CharField(max_length=255, blank=True, null=True, default='')
    mem1_name = models.CharField(max_length=255, blank=True, null=True, default='')
    mem1_stuID = models.CharField(max_length=255, blank=True, null=True, default='')
    mem1_institute = models.CharField(max_length=255, blank=True, null=True, default='')
    mem1_major_class = models.CharField(max_length=255, blank=True, null=True, default='')
    mem1_job = models.CharField(max_length=255, blank=True, null=True, default='')
    mem2_name = models.CharField(max_length=255, blank=True, null=True, default='')
    mem2_stuID = models.CharField(max_length=255, blank=True, null=True, default='')
    mem2_institute = models.CharField(max_length=255, blank=True, null=True, default='')
    mem2_major_class = models.CharField(max_length=255, blank=True, null=True, default='')
    mem2_job = models.CharField(max_length=255, blank=True, null=True, default='')
    mem3_name = models.CharField(max_length=255, blank=True, null=True, default='')
    mem3_stuID = models.CharField(max_length=255, blank=True, null=True, default='')
    mem3_institute = models.CharField(max_length=255, blank=True, null=True, default='')
    mem3_major_class = models.CharField(max_length=255, blank=True, null=True, default='')
    mem3_job = models.CharField(max_length=255, blank=True, null=True, default='')
    mem4_name = models.CharField(max_length=255, blank=True, null=True, default='')
    mem4_stuID = models.CharField(max_length=255, blank=True, null=True, default='')
    mem4_institute = models.CharField(max_length=255, blank=True, null=True, default='')
    mem4_major_class = models.CharField(max_length=255, blank=True, null=True, default='')
    mem4_job = models.CharField(max_length=255, blank=True, null=True, default='')
    pro_lab = models.TextField(blank=True, null=True, default='')
    pro_instrument = models.TextField(blank=True, null=True, default='')
    pro_hours = models.CharField(max_length=255, blank=True, null=True, default='')
    pro_period = models.CharField(max_length=255, blank=True, null=True, default='')
    pro_status = models.CharField(max_length=255, blank=True, null=True, default='')
    pro_sum = models.CharField(max_length=255, blank=True, null=True, default='')
    money_in = models.CharField(max_length=255, blank=True, null=True, default='')
    money_in_remark = models.CharField(max_length=255, blank=True, null=True, default='')
    money_consume = models.CharField(max_length=255, blank=True, null=True, default='')
    money_consume_remark = models.CharField(max_length=255, blank=True, null=True, default='')
    money_allowance = models.CharField(max_length=255, blank=True, null=True, default='')
    money_allowance_remark = models.CharField(max_length=255, blank=True, null=True, default='')
    money_other = models.CharField(max_length=255, blank=True, null=True, default='')
    money_other_remark = models.CharField(max_length=255, blank=True, null=True, default='')
    money_total = models.CharField(max_length=255, blank=True, null=True, default='')
    money_total_remark = models.CharField(max_length=255, blank=True, null=True, default='')
    money_rest = models.CharField(max_length=255, blank=True, null=True, default='')
    money_rest_remark = models.CharField(max_length=255, blank=True, null=True, default='')

    class Meta:
        managed = False
        db_table = 'conclude'



class Apply(models.Model):
    pro_id = models.IntegerField(primary_key=True)
    export_time = models.CharField(max_length=255, blank=True, null=True, default='')
    status = models.CharField(max_length=1, blank=True, null=True, default='')
    leader_id = models.CharField(max_length=255, blank=True, null=True, default='')
    fillin_time = models.CharField(max_length=255, blank=True, null=True, default='')
    pro_way = models.CharField(max_length=255, blank=True, null=True, default='')
    search_area = models.CharField(max_length=255, blank=True, null=True, default='')
    tutor_area = models.CharField(max_length=255, blank=True, null=True, default='')
    tutor_phone = models.CharField(max_length=255, blank=True, null=True, default='')
    tutor_email = models.CharField(max_length=255, blank=True, null=True, default='')
    leader_grade = models.CharField(max_length=255, blank=True, null=True, default='')
    leader_area = models.CharField(max_length=255, blank=True, null=True, default='')
    leader_job = models.CharField(max_length=255, blank=True, null=True, default='')
    mem1_name = models.CharField(max_length=255, blank=True, null=True, default='')
    mem1_sex = models.CharField(max_length=255, blank=True, null=True, default='')
    mem1_stuID = models.CharField(max_length=255, blank=True, null=True, default='')
    mem1_grade = models.CharField(max_length=255, blank=True, null=True, default='')
    mem1_area = models.CharField(max_length=255, blank=True, null=True, default='')
    mem1_job = models.CharField(max_length=255, blank=True, null=True, default='')
    mem1_institute = models.CharField(max_length=255, blank=True, null=True, default='')
    mem2_name = models.CharField(max_length=255, blank=True, null=True, default='')
    mem2_sex = models.CharField(max_length=255, blank=True, null=True, default='')
    mem2_stuID = models.CharField(max_length=255, blank=True, null=True, default='')
    mem2_grade = models.CharField(max_length=255, blank=True, null=True, default='')
    mem2_area = models.CharField(max_length=255, blank=True, null=True, default='')
    mem2_job = models.CharField(max_length=255, blank=True, null=True, default='')
    mem2_institute = models.CharField(max_length=255, blank=True, null=True, default='')
    mem3_name = models.CharField(max_length=255, blank=True, null=True, default='')
    mem3_sex = models.CharField(max_length=255, blank=True, null=True, default='')
    mem3_stuID = models.CharField(max_length=255, blank=True, null=True, default='')
    mem3_grade = models.CharField(max_length=255, blank=True, null=True, default='')
    mem3_area = models.CharField(max_length=255, blank=True, null=True, default='')
    mem3_job = models.CharField(max_length=255, blank=True, null=True, default='')
    mem3_institute = models.CharField(max_length=255, blank=True, null=True, default='')
    pro_reason = models.TextField(blank=True, null=True, default='')
    pro_content = models.TextField(blank=True, null=True, default='')
    pro_innovation = models.TextField(blank=True, null=True, default='')
    pro_source = models.TextField(blank=True, null=True, default='')
    time1 = models.CharField(max_length=255, blank=True, null=True, default='')
    content1 = models.CharField(max_length=255, blank=True, null=True, default='')
    leader1 = models.CharField(max_length=255, blank=True, null=True, default='')
    time2 = models.CharField(max_length=255, blank=True, null=True, default='')
    time3 = models.CharField(max_length=255, blank=True, null=True, default='')
    time4 = models.CharField(max_length=255, blank=True, null=True, default='')
    time5 = models.CharField(max_length=255, blank=True, null=True, default='')
    time6 = models.CharField(max_length=255, blank=True, null=True, default='')
    time7 = models.CharField(max_length=255, blank=True, null=True, default='')
    content2 = models.CharField(max_length=255, blank=True, null=True, default='')
    content3 = models.CharField(max_length=255, blank=True, null=True, default='')
    content4 = models.CharField(max_length=255, blank=True, null=True, default='')
    content5 = models.CharField(max_length=255, blank=True, null=True, default='')
    content6 = models.CharField(max_length=255, blank=True, null=True, default='')
    content7 = models.CharField(max_length=255, blank=True, null=True, default='')
    leader2 = models.CharField(max_length=255, blank=True, null=True, default='')
    leader3 = models.CharField(max_length=255, blank=True, null=True, default='')
    leader4 = models.CharField(max_length=255, blank=True, null=True, default='')
    leader5 = models.CharField(max_length=255, blank=True, null=True, default='')
    leader6 = models.CharField(max_length=255, blank=True, null=True, default='')
    leader7 = models.CharField(max_length=255, blank=True, null=True, default='')
    pro_achievement = models.CharField(max_length=255, blank=True, null=True, default='')
    pro_endtime = models.CharField(max_length=255, blank=True, null=True, default='')
    pro_form = models.CharField(max_length=255, blank=True, null=True, default='')
    pro_participant = models.CharField(max_length=255, blank=True, null=True, default='')
    budget_equip_money = models.CharField(max_length=255, blank=True, null=True, default='')
    budget_equip_reason = models.CharField(max_length=255, blank=True, null=True, default='')
    budget_material_money = models.CharField(max_length=255, blank=True, null=True, default='')
    budget_material_reason = models.CharField(max_length=255, blank=True, null=True, default='')
    budget_meeting_money = models.CharField(max_length=255, blank=True, null=True, default='')
    budget_meeting_reason = models.CharField(max_length=255, blank=True, null=True, default='')
    budget_apply_money = models.CharField(max_length=255, blank=True, null=True, default='')
    budget_apply_reason = models.CharField(max_length=255, blank=True, null=True, default='')
    budget_books_money = models.CharField(max_length=255, blank=True, null=True, default='')
    budget_books_reason = models.CharField(max_length=255, blank=True, null=True, default='')
    budget_trans_money = models.CharField(max_length=255, blank=True, null=True, default='')
    budget_trans_reason = models.CharField(max_length=255, blank=True, null=True, default='')
    budget_service_money = models.CharField(max_length=255, blank=True, null=True, default='')
    budget_service_reason = models.CharField(max_length=255, blank=True, null=True, default='')
    budget_other_money = models.CharField(max_length=255, blank=True, null=True, default='')
    budget_other_reason = models.CharField(max_length=255, blank=True, null=True, default='')
    budget_total_money = models.CharField(max_length=255, blank=True, null=True, default='')

    class Meta:
        managed = False
        db_table = 'apply'


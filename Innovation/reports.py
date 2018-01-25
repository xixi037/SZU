from django.http import HttpResponseRedirect

from Innovation.models import Middle, ProInfo, Conclude


def todict(source):
    target = {}
    for item in source:
        target.__setitem__(item.get('name'), item.get('value'))
    return target

def save_middle(request):
    if request.POST.get('info', '') != '':
        info = eval(request.POST.get('info'))
        info = todict(info)
        pro_num = info.get('pro_num', '')
        leader_stuID = info.get('leader_stuID', '')
        # leader_phone = info.get('leader_phone', '')
        pro_mems = info.get('pro_mems', '')
        # tutor_name = info.get('tutor_name', '')
        pro_stime = info.get('pro_stime', '')
        pro_etime = info.get('pro_etime', '')
        pro_endtime = info.get('pro_endtime', '')
        pro_schedule = info.get('pro_schedule', '')
        pro_source = info.get('pro_source', '')
        pro_money = info.get('pro_money', '')
        pro_difficulties = info.get('pro_difficulties', '')
        pro_advice = info.get('pro_advice', '')
        pro_change = info.get('pro_change', '')
        pro_plan = info.get('pro_plan', '')
        pro_harvest = info.get('pro_harvest', '')
        status = info.get('status')

        print(leader_stuID)
        if Middle.objects.filter(leader_id=leader_stuID):
            Middle.objects.filter(leader_id=leader_stuID).update(pro_num=pro_num, pro_mems=pro_mems,
                                                                 pro_stime=pro_stime, pro_etime=pro_etime,
                                                                 pro_endtime=pro_endtime,
                                                                 pro_schedule=pro_schedule, pro_source=pro_source,
                                                                 pro_money=pro_money, pro_difficulties=pro_difficulties,
                                                                 pro_advice=pro_advice, pro_change=pro_change,
                                                                 pro_plan=pro_plan, pro_harvest=pro_harvest,
                                                                 status=status)
        else:
            if ProInfo.objects.filter(leader_id=leader_stuID):
                pro_object = ProInfo.objects.filter(leader_id=leader_stuID)
                for i in pro_object:
                    pro_id = i.id
                Middle.objects.create(pro_id=pro_id, leader_id=leader_stuID, pro_num=pro_num, pro_mems=pro_mems,
                                      pro_stime=pro_stime, pro_etime=pro_etime, pro_endtime=pro_endtime,
                                      pro_schedule=pro_schedule, pro_source=pro_source, pro_money=pro_money,
                                      pro_difficulties=pro_difficulties,
                                      pro_advice=pro_advice, pro_change=pro_change, pro_plan=pro_plan,
                                      pro_harvest=pro_harvest, status=status)
            else:
                return HttpResponseRedirect('404.html')

        print('填写完毕')
    return HttpResponseRedirect('/middle')



def save_conclude(request):
    print('保存结题报告啦')
    if request.POST.get('info', '') != '':
        info = eval(request.POST.get('info'))
        info = todict(info)
        pro_num = info.get('pro_num', '')
        pro_time = info.get('pro_time', '')
        leader_id = info.get('leader_id', '')
        leader_ethnicity = info.get('leader_ethnicity', '')
        leader_birth = info.get('leader_birth', '')
        leader_address = info.get('leader_address', '')
        leader_institute = info.get('leader_institute', '')
        leader_job = info.get('leader_job', '')
        mem1_name = info.get('mem1_name', '')
        mem1_stuID = info.get('mem1_stuID', '')
        mem1_institute = info.get('mem1_institute', '')
        mem1_major_class = info.get('mem1_major_class', '')
        mem1_job = info.get('mem1_job', '')
        mem2_name = info.get('mem2_name', '')
        mem2_stuID = info.get('mem2_stuID', '')
        mem2_institute = info.get('mem2_institute','')
        mem2_major_class = info.get('mem2_major_class', '')
        mem2_job = info.get('mem2_job', '')
        mem3_name = info.get('mem3_name', '')
        mem3_stuID = info.get('mem3_stuID', '')
        mem3_institute = info.get('mem3_institute', '')
        mem3_major_class = info.get('mem3_major_class', '')
        mem3_job = info.get('mem3_job', '')
        mem4_name = info.get('mem4_name', '')
        mem4_stuID = info.get('mem4_stuID', '')
        mem4_institute = info.get('mem4_institute', '')
        mem4_major_class = info.get('mem4_major_class', '')
        mem4_job = info.get('mem4_job', '')
        pro_lab = info.get('pro_lab', '')
        pro_instrument = info.get('pro_instrument', '')
        pro_hours = info.get('pro_hours', '')
        pro_period = info.get('pro_period', '')
        pro_status = info.get('pro_status', '')
        pro_sum = info.get('pro_sum', '')
        money_in = info.get('money_in', '')
        money_in_remark = info.get('money_in_remark', '')
        money_consume = info.get('money_consume', '')
        money_consume_remark = info.get('money_consume_remark', '')
        money_allowance = info.get('money_allowance', '')
        money_allowance_remark = info.get('money_allowance_remark', '')
        money_other = info.get('money_other', '')
        money_other_remark = info.get('money_other_remark', '')
        money_total = info.get('money_total', '')
        money_total_remark = info.get('money_total_remark', '')
        money_rest = info.get('money_rest', '')
        money_rest_remark = info.get('money_rest_remark', '')
        status = info.get('status')

        if Conclude.objects.filter(leader_id=leader_id):
            Conclude.objects.filter(leader_id=leader_id).update(pro_num=pro_num, pro_time=pro_time,status=status,
                                                              leader_ethnicity=leader_ethnicity, leader_birth=leader_birth,
                                                              leader_address=leader_address, leader_institute=leader_institute,
                                                              leader_job=leader_job,mem1_name=mem1_name, mem1_stuID=mem1_stuID,
                                                              mem1_institute=mem1_institute, mem1_major_class=mem1_major_class,
                                                              mem1_job=mem1_job,mem2_name=mem2_name,mem2_stuID=mem2_stuID,
                                                              mem2_institute=mem2_institute,mem2_major_class=mem2_major_class,
                                                              mem2_job=mem2_job,mem3_name=mem3_name,mem3_stuID=mem3_stuID,
                                                              mem3_institute=mem3_institute,mem3_major_class=mem3_major_class,
                                                              mem3_job=mem3_job,mem4_name=mem4_name,mem4_stuID=mem4_stuID,
                                                              mem4_institute=mem4_institute,mem4_major_class=mem4_major_class,
                                                              mem4_job=mem4_job,pro_lab=pro_lab,pro_instrument=pro_instrument,
                                                              pro_hours=pro_hours,pro_period=pro_period,pro_status=pro_status,
                                                              pro_sum=pro_sum,money_in=money_in,money_in_remark=money_in_remark,
                                                              money_consume=money_consume,money_consume_remark=money_consume_remark,
                                                              money_allowance=money_allowance,money_allowance_remark=money_allowance_remark,
                                                              money_other=money_other,money_other_remark=money_other_remark,money_total=money_total,
                                                              money_total_remark=money_total_remark,money_rest=money_rest,money_rest_remark=money_rest_remark)
        else:
            if ProInfo.objects.filter(leader_id=leader_id):
                pro_object = ProInfo.objects.filter(leader_id=leader_id)
                for i in pro_object:
                    pro_id = i.id
                    Conclude.objects.create(pro_id=pro_id,pro_num=pro_num, pro_time=pro_time,leader_id=leader_id,
                                      leader_ethnicity=leader_ethnicity, leader_birth=leader_birth,status=status,
                                      leader_address=leader_address, leader_institute=leader_institute,
                                      leader_job=leader_job,mem1_name=mem1_name, mem1_stuID=mem1_stuID,
                                      mem1_institute=mem1_institute, mem1_major_class=mem1_major_class,
                                      mem1_job=mem1_job,mem2_name=mem2_name,mem2_stuID=mem2_stuID,
                                      mem2_institute=mem2_institute,mem2_major_class=mem2_major_class,
                                      mem2_job=mem2_job,mem3_name=mem3_name,mem3_stuID=mem3_stuID,
                                      mem3_institute=mem3_institute,mem3_major_class=mem3_major_class,
                                      mem3_job=mem3_job,mem4_name=mem4_name,mem4_stuID=mem4_stuID,
                                      mem4_institute=mem4_institute,mem4_major_class=mem4_major_class,
                                      mem4_job=mem4_job,pro_lab=pro_lab,pro_instrument=pro_instrument,
                                      pro_hours=pro_hours,pro_period=pro_period,pro_status=pro_status,
                                      pro_sum=pro_sum,money_in=money_in,money_in_remark=money_in_remark,
                                      money_consume=money_consume,money_consume_remark=money_consume_remark,
                                      money_allowance=money_allowance,money_allowance_remark=money_allowance_remark,
                                      money_other=money_other,money_other_remark=money_other_remark,money_total=money_total,
                                      money_total_remark=money_total_remark,money_rest=money_rest,money_rest_remark=money_rest_remark)
            else:
                return HttpResponseRedirect('404.html')

        print('填写完毕')
    return HttpResponseRedirect('/conclude')



from django.http import HttpResponseRedirect

from Innovation.models import Middle, ProInfo


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



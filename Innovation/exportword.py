import os
from django.http import HttpResponse

import pythoncom
import time
import win32com.client

from Innovation.models import Middle, Users, ProInfo


def todict(source):
    target = {}
    for item in source:
        target.__setitem__(item.get('name'), item.get('value'))
    return target

def write_to_middle(id):
    print('到这里了')
    print(id)

    if Middle.objects.filter(leader_id=id):
        middle_info = Middle.objects.filter(leader_id=id)
        user_info = Users.objects.filter(username=id)
        for i in middle_info:
            pro_info = ProInfo.objects.filter(id=i.pro_id)

        for info in middle_info:
            filename = '中期报告模板.doc'
            open_path = os.getcwd() + os.sep + 'models'
            save_path = os.getcwd() + os.sep + 'middle'
            if not os.path.exists(open_path):
                os.makedirs(open_path)
            file = os.path.join(open_path, filename)
            print(file)

            for info1 in pro_info:
                pro_name = info1.pro_name
                tutor_name = info1.tutor_id

            for info2 in user_info:
                pro_leader = info2.name

            savename = '中期报告_' + tutor_name + '_' + pro_leader + '_' + pro_name + '.doc'

            savepath = os.path.join(save_path, savename)
            if os.path.exists(savepath):
                print('路径是...')
                print(savepath.encode('utf-8'))
                return HttpResponse(savepath.encode('utf-8'))

            pythoncom.CoInitialize()
            try:
                app = win32com.client.Dispatch('word.Application')
                doc = app.Documents.Open(file)
                print('打开的是word')
            except:
                app = win32com.client.Dispatch('kwps.Application')
                doc = app.Documents.Open(file)
                print('打开的是wps')


            # 第一张表填写位置
            t1 = doc.Tables[0]
            pro_num_pos = t1.Cell(1, 2)
            pro_name_pos = t1.Cell(1, 4)
            pro_leader_pos = t1.Cell(2, 2)
            leader_stuID_pos = t1.Cell(2, 4)
            leader_phone_pos = t1.Cell(2, 6)
            pro_mems_pos = t1.Cell(3,2)
            tutor_name_pos = t1.Cell(4, 2)
            pro_period_pos = t1.Cell(5,2)
            pro_endtime_pos = t1.Cell(5,4)
            pro_schedule_pos = t1.Cell(6, 1)
            pro_source_pos = t1.Cell(7, 1)
            pro_money_pos = t1.Cell(8, 1)
            pro_difficulties_pos = t1.Cell(9, 1)
            pro_advice_pos = t1.Cell(10,1)
            pro_change_pos = t1.Cell(11, 1)
            pro_plan_pos = t1.Cell(12, 1)
            pro_harvest_pos = t1.Cell(13, 1)

            pro_num_pos.Range.Text = info.pro_num
            leader_stuID_pos.Range.Text = info.leader_id
            pro_mems_pos.Range.Text = info.pro_mems
            pro_period_pos.Range.Text = info.pro_stime + '至' + info.pro_etime
            pro_endtime_pos.Range.Text = info.pro_endtime

            schedule_title = str(pro_schedule_pos).replace('\r', '')
            source_title = str(pro_source_pos).replace('\r', '')
            money_title = str(pro_money_pos).replace('\r', '')
            difficulties_title = str(pro_difficulties_pos).replace('\r', '')
            advice_title = str(pro_advice_pos).replace('\r', '')
            change_title = str(pro_change_pos).replace('\r', '')
            plan_title = str(pro_plan_pos).replace('\r', '')
            harvest_title = str(pro_harvest_pos).replace('\r', '')
            if info.pro_schedule.strip() != '':
                pro_schedule_pos.Range.Text = schedule_title + '\n' + info.pro_schedule
            if info.pro_source.strip() != '':
                pro_source_pos.Range.Text = source_title + '\n' + info.pro_source
            if info.pro_money.strip() != '':
                pro_money_pos.Range.Text = money_title + '\n' + info.pro_money
            if info.pro_difficulties.strip() != '':
                pro_difficulties_pos.Range.Text = difficulties_title + '\n' + info.pro_difficulties
            if info.pro_advice.strip() != '':
                pro_advice_pos.Range.Text = advice_title + '\n' + info.pro_advice
            if info.pro_change.strip() != '':
                pro_change_pos.Range.Text = change_title + '\n' + info.pro_change
            if info.pro_plan.strip() != '':
                pro_plan_pos.Range.Text = plan_title + '\n' + info.pro_plan
            if info.pro_harvest.strip() != '':
                pro_harvest_pos.Range.Text = harvest_title + '\n' + info.pro_harvest

            for info in pro_info:
                pro_name_pos.Range.Text = info.pro_name
                tutor_name_pos.Range.Text = info.tutor_id
            for info in user_info:
                pro_leader_pos.Range.Text = info.name
                leader_phone_pos.Range.Text = info.phone


        doc.SaveAs(savepath)
        doc.Close()
        app.Quit()
        print('保存完毕')
        date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        Middle.objects.filter(leader_id=id).update(export_time=date)
        return HttpResponse(savepath.encode('utf-8'))
    return 'error'
import os
from django.http import HttpResponse, JsonResponse

import pythoncom
import time
import win32com.client

from Innovation.models import Middle, Users, ProInfo, Conclude


def tolist(source):
    list = []
    for item in source:
        list.append(item.get('value'))
    return list

def todict(source):
    target = {}
    for item in source:
        target.__setitem__(item.get('name'), item.get('value'))
    return target

def write_to_middle(request):
    if request.POST.get('choicelist','') != '':
        choicelist = eval(request.POST.get('choicelist'))[1:]
        print(choicelist)
        choicelist = tolist(choicelist)
        pathlist = []
        for id in choicelist:
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
                    if os.path.exists(savepath) is False:

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
                print(savepath.encode('utf-8'))
                pathlist.append(savepath)
        print(pathlist)
        pathdic = {"path":pathlist}
        print('路径dic为：')
        print(pathdic)
        return JsonResponse(pathdic)
    return 'error'

def write_to_conclude(request):
    print('写结题报告啦')
    if request.POST.get('choicelist','') != '':
        choicelist = eval(request.POST.get('choicelist'))[1:]
        print(choicelist)
        choicelist = tolist(choicelist)
        pathlist = []
        for id in choicelist:
            if Conclude.objects.filter(leader_id=id):
                conclude_info = Conclude.objects.filter(leader_id=id)
                user_info = Users.objects.filter(username=id)
                for i in conclude_info:
                    pro_info = ProInfo.objects.filter(id=i.pro_id)

                for info in conclude_info:
                    filename = '结题报告模板.doc'
                    open_path = os.getcwd() + os.sep + 'models'
                    save_path = os.getcwd() + os.sep + 'conclude'
                    if not os.path.exists(open_path):
                        os.makedirs(open_path)
                    file = os.path.join(open_path, filename)
                    print(file)

                    for info1 in pro_info:
                        pro_name = info1.pro_name
                        tutor_name = info1.tutor_id

                    for info2 in user_info:
                        pro_leader = info2.name
                        leader_phone = info2.name
                        leader_sex = info2.sex
                        email = info2.email
                        major = info2.major
                        classID = info2.classID

                    date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
                    savename = '结题报告_' + tutor_name + '_' + pro_leader + '_' + pro_name + '.doc'

                    savepath = os.path.join(save_path, savename)
                    if os.path.exists(savepath) is False:

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
                        pro_name_pos = t1.Cell(2, 2)
                        pro_leader_pos = t1.Cell(3, 2)
                        leader_phone_pos = t1.Cell(4, 2)
                        tutor_id_pos = t1.Cell(5, 2)
                        leader_units_pos = t1.Cell(6, 2)
                        pro_time_pos = t1.Cell(7, 2)
                        apply_time_pos = t1.Cell(8, 2)

                        pro_num_pos.Range.ParagraphFormat.Alignment = 1
                        pro_num_pos.Range.Text = info.pro_num
                        pro_name_pos.Range.ParagraphFormat.Alignment = 1
                        pro_name_pos.Range.Text = pro_name
                        pro_leader_pos.Range.ParagraphFormat.Alignment = 1
                        pro_leader_pos.Range.Text = pro_leader
                        leader_phone_pos.Range.ParagraphFormat.Alignment = 1
                        leader_phone_pos.Range.Text = leader_phone
                        tutor_id_pos.Range.ParagraphFormat.Alignment = 1
                        tutor_id_pos.Range.Text = tutor_name
                        leader_units_pos.Range.ParagraphFormat.Alignment = 1
                        leader_units_pos.Range.Text = "深圳大学"
                        pro_time_pos.Range.ParagraphFormat.Alignment = 1
                        pro_time_pos.Range.Text = info.pro_time
                        apply_time_pos.Range.ParagraphFormat.Alignment = 1
                        apply_time_pos.Range.Text = date

                        t2 = doc.Tables[1]
                        pro_name1_pos = t2.Cell(1, 2)
                        pro_leader1_pos = t2.Cell(2, 3)
                        leader_sex_pos = t2.Cell(2, 5)
                        leader_ethnicity_pos = t2.Cell(2, 7)
                        leader_birth_pos = t2.Cell(2, 9)
                        leader_units1_pos = t2.Cell(3, 3)
                        leader_id_pos = t2.Cell(3, 5)
                        leader_address_pos = t2.Cell(4, 3)
                        email_pos = t2.Cell(4, 5)
                        leader_phone1_pos = t2.Cell(5, 3)

                        pro_name1_pos.Range.Text = pro_name
                        pro_leader1_pos.Range.Text = pro_leader
                        leader_sex_pos.Range.Text = leader_sex
                        leader_ethnicity_pos.Range.Text = info.leader_ethnicity
                        leader_birth_pos.Range.Text = info.leader_birth
                        leader_units1_pos.Range.Text = "深圳大学"
                        leader_id_pos.Range.Text = info.leader_id
                        leader_address_pos.Range.Text = info.leader_address
                        email_pos.Range.Text = email
                        leader_phone1_pos.Range.Text = leader_phone

                        pro_leader2_pos = t2.Cell(7, 2)
                        leader_id1_pos = t2.Cell(7, 3)
                        leader_institute_pos = t2.Cell(7, 4)
                        leader_major_class_pos = t2.Cell(7, 5)
                        leader_job_pos = t2.Cell(7, 6)
                        mem1_name_pos = t2.Cell(8, 2)
                        mem1_stuID_pos = t2.Cell(8, 3)
                        mem1_institute_pos = t2.Cell(8, 4)
                        mem1_major_class_pos = t2.Cell(8, 5)
                        mem1_job_pos = t2.Cell(8, 6)
                        mem2_name_pos = t2.Cell(9, 2)
                        mem2_stuID_pos = t2.Cell(9, 3)
                        mem2_institute_pos = t2.Cell(9, 4)
                        mem2_major_class_pos = t2.Cell(9, 5)
                        mem2_job_pos = t2.Cell(9, 6)
                        mem3_name_pos = t2.Cell(10, 2)
                        mem3_stuID_pos = t2.Cell(10, 3)
                        mem3_institute_pos = t2.Cell(10, 4)
                        mem3_major_class_pos = t2.Cell(10, 5)
                        mem3_job_pos = t2.Cell(10, 6)
                        mem4_name_pos = t2.Cell(11, 2)
                        mem4_stuID_pos = t2.Cell(11, 3)
                        mem4_institute_pos = t2.Cell(11, 4)
                        mem4_major_class_pos = t2.Cell(11, 5)
                        mem4_job_pos = t2.Cell(11, 6)

                        pro_leader2_pos.Range.Text = pro_leader
                        leader_id1_pos.Range.Text = info.leader_id
                        leader_institute_pos.Range.Text = info.leader_institute
                        leader_major_class_pos.Range.Text = major + classID
                        leader_job_pos.Range.Text = info.leader_job
                        mem1_name_pos.Range.Text = info.mem1_name
                        mem1_stuID_pos.Range.Text = info.mem1_stuID
                        mem1_institute_pos.Range.Text = info.mem1_institute
                        mem1_major_class_pos.Range.Text = info.mem1_major_class
                        mem1_job_pos.Range.Text = info.mem1_job
                        mem2_name_pos.Range.Text = info.mem2_name
                        mem2_stuID_pos.Range.Text = info.mem2_stuID
                        mem2_institute_pos.Range.Text = info.mem2_institute
                        mem2_major_class_pos.Range.Text = info.mem2_major_class
                        mem2_job_pos.Range.Text = info.mem2_job
                        mem3_name_pos.Range.Text = info.mem3_name
                        mem3_stuID_pos.Range.Text = info.mem3_stuID
                        mem3_institute_pos.Range.Text = info.mem3_institute
                        mem3_major_class_pos.Range.Text = info.mem3_major_class
                        mem3_job_pos.Range.Text = info.mem3_job
                        mem4_name_pos.Range.Text = info.mem4_name
                        mem4_stuID_pos.Range.Text = info.mem4_stuID
                        mem4_institute_pos.Range.Text = info.mem4_institute
                        mem4_major_class_pos.Range.Text = info.mem4_major_class
                        mem4_job_pos.Range.Text = info.mem4_job

                        pro_lab_pos = t2.Cell(15, 2)
                        pro_instrument_pos = t2.Cell(16, 2)
                        pro_hours_pos = t2.Cell(17, 2)
                        pro_period_status_pos = t2.Cell(19, 2)
                        pro_sum_pos = t2.Cell(21, 2)

                        pro_lab_pos.Range.Text = info.pro_lab
                        pro_instrument_pos.Range.Text = info.pro_instrument
                        # pro_hours_pos.Range.Style.Font.Underline = 1
                        pro_hours_pos.Range.InsertAfter(info.pro_hours + '小时')
                        # pro_period_status_pos.Range.Style.Font.Underline = 1
                        pro_period_status_pos.Range.InsertAfter(info.pro_period)
                        # pro_period_status_pos.Range.Style.Font.Underline = 0
                        pro_period_status_pos.Range.InsertAfter("完成情况：1.提前 2.按时 3.延期")
                        # pro_period_status_pos.Range.Style.Font.Underline = 1
                        pro_period_status_pos.Range.InsertAfter(info.pro_status)

                        pro_sum_pos.Range.Text = info.pro_sum

                        money_in_pos = t2.Cell(23, 3)
                        money_in_remark_pos = t2.Cell(23, 4)
                        money_consume_pos = t2.Cell(25, 3)
                        money_consume_remark_pos = t2.Cell(25, 4)
                        money_allowance_pos = t2.Cell(26, 3)
                        money_allowance_remark_pos = t2.Cell(26, 4)
                        money_other_pos = t2.Cell(27, 3)
                        money_other_remark_pos = t2.Cell(27, 4)
                        money_total_pos = t2.Cell(28, 3)
                        money_total_remark_pos = t2.Cell(28, 4)
                        money_rest_pos = t2.Cell(29, 3)
                        money_rest_remark_pos = t2.Cell(29, 4)

                        money_in_pos.Range.Text = info.money_in
                        money_in_remark_pos.Range.Text = info.money_in_remark
                        money_consume_pos.Range.Text = info.money_consume
                        money_consume_remark_pos.Range.Text = info.money_consume_remark
                        money_allowance_pos.Range.Text = info.money_allowance
                        money_allowance_remark_pos.Range.Text = info.money_allowance_remark
                        money_other_pos.Range.Text = info.money_other
                        money_other_remark_pos.Range.Text = info.money_other_remark
                        money_total_pos.Range.Text = info.money_total
                        money_total_remark_pos.Range.Text = info.money_total_remark
                        money_rest_pos.Range.Text = info.money_rest
                        money_rest_remark_pos.Range.Text = info.money_rest_remark

                        doc.SaveAs(savepath)
                        doc.Close()
                        app.Quit()
                        print('保存完毕')
                        # date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
                        Conclude.objects.filter(leader_id=id).update(export_time=date)
                print(savepath.encode('utf-8'))
                pathlist.append(savepath)
        print(pathlist)
        pathdic = {"path":pathlist}
        print('路径dic为：')
        print(pathdic)
        return JsonResponse(pathdic)
    return 'error'
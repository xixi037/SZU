from __future__ import unicode_literals
# coding=utf-8
import time
import os
from django.forms import model_to_dict
from email.header import make_header

from django.core.mail import EmailMultiAlternatives

from django.http import HttpResponseRedirect, HttpResponse, StreamingHttpResponse, JsonResponse
from django.shortcuts import render

from Innovation.models import Users, Middle, ProInfo, Managers, Members, Status

def nav_status(request):
    status = Status.objects.all()[0]
    mode = status.mode
    date_object = Status.objects.all()[0]
    date = str(date_object.date)
    date = date.replace("-", "")
    statusdic = {'status':mode,'date':date}
    return JsonResponse(statusdic)


def base(request):
    username = request.COOKIES.get('username')
    if ProInfo.objects.filter(leader_id=username):
        # status = Status.objects.all()[0]
        # mode = status.mode
        # date1 = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        # date1 = date1.replace("-", "")
        # date = Status.objects.all()[0]
        # date2 = str(date.date)
        # date2 = date2.replace("-", "")
        # return render(request, 'base.html', {'username': username, 'status': mode, 'date': date1 <= date2})
        return render(request,'base.html')
    else:
        return HttpResponseRedirect('/index')






def success(request):
    response = render(request, 'achieve.html')
    if request.GET.get('url', '') != '':
        url = request.GET.get('url')
        response = render(request, 'achieve.html', {'url': url})
    return response





def downloadFile(request):
    if request.GET.get('url', '') != '':
        print('有参数啦')
        filename = request.GET["url"]
        file_name = filename.split(os.sep)[-1]
        print(filename)
        # filenamelist = [r'C:\Users\HP\Desktop\SZU\middle\中期报告_邓云_陈希曦_基于Python的网络爬虫.doc',r'C:\Users\HP\Desktop\SZU\middle\中期报告_邓云_黄树华_基于深度学习的肌电图、脑电图分析2.doc']
        # for filename in filenamelist:
        file_name = filename.split(os.sep)[-1]
        def file_iterator(file_name, chunk_size=512):
            with open(file_name, 'rb') as f:
                while True:
                    c = f.read(chunk_size)
                    if c:
                        yield c
                    else:
                        break

        response = StreamingHttpResponse(file_iterator(filename))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename=' + file_name.encode('utf-8').decode('ISO-8859-1')
        return response
    return HttpResponseRedirect('/success')


def check(request):
    print('检查了')
    if request.method == 'POST':
        username = request.POST['username']
        print(username)
        password = request.POST['password']
        print(password)
        user = Users.objects.filter(username__exact=username, password__exact=password)
        if user:
            print('存在')
            flag = 1

            if ProInfo.objects.filter(leader_id=username):
                response = HttpResponseRedirect('/base')
            else:
                response = HttpResponseRedirect('/index')
            response.set_cookie('username', username, 3600)
            response.set_cookie('flag', flag, 3600)
            return response
        else:
            return HttpResponseRedirect('/login')


def login(request):
    return render(request, 'login.html')


def basic(request):
    date1 = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    date1 = date1.replace("-", "")
    date = Status.objects.all()[0]
    date2 = str(date.date)
    date2 = date2.replace("-", "")
    if date1>date2:
        return HttpResponseRedirect('/base')
    if Status.objects.filter():
        username = request.COOKIES.get('username')
        if request.GET.get('from', '') == 'base':
            user_info = Users.objects.get(username=username)
            pro_info = ProInfo.objects.get(leader_id=username)
            mem_info = Members.objects.filter(pro_id=pro_info.id)
            memlist = []
            for i in mem_info:
                memlist.append(i.stu_id)
            memlist = '/'.join(memlist)
            return render(request, 'basic.html', {'user_info': user_info, 'pro_info': pro_info, 'memlist': memlist})
        elif ProInfo.objects.filter(leader_id=username):
            return HttpResponseRedirect('/base')
        else:
            user_info = Users.objects.get(username=username)
            return render(request, 'basic.html', {'user_info': user_info})
    return HttpResponseRedirect('/login')





def welcome(request):
    username = request.COOKIES.get('username')
    if ProInfo.objects.filter(leader_id=username):
        status = Status.objects.all()[0]
        mode = status.mode
        date1 = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        date1 = date1.replace("-", "")
        date = Status.objects.all()[0]
        date2 = str(date.date)
        date2 = date2.replace("-", "")
        return render(request, 'welcome.html', {'username': username, 'status': mode,'date':date1<=date2})
    else:
        return HttpResponseRedirect('/index')


def cancel(request):
    response = HttpResponse('cancel')
    response.set_cookie('username', '')
    response.set_cookie('flag', '')
    return response


def upload_apply(request):
    return render(request, 'upload_apply.html')


def getfile(request):
    if request.FILES.get('file', '') != '':
        file_obj = request.FILES.get('file')
        if request.COOKIES.get('username', '') != '':
            username = request.COOKIES.get('username')
            user_info = Users.objects.filter(username=username)
            print(username)
            if user_info:
                for i in user_info:
                    if i.pro_name:
                        name = i.name
                        tutor_name = i.tutor_name
                        pro_name = i.pro_name
                    else:
                        return HttpResponseRedirect('/base')
                    path = os.getcwd() + os.sep + 'applications'
                    savename = '申请书_' + tutor_name + '_' + name + '_' + pro_name + '.doc'
                    filepath = os.path.join(path, savename)
                    print(filepath)
                    dest = open(filepath, 'wb+')
                    dest.write(file_obj.read())
                    dest.close()
            return render(request, 'base.html', {'username': username})
        return HttpResponseRedirect('/login')
    return HttpResponseRedirect('/upload')


def change_password(request):
    return render(request, 'change_password.html')


def check_password(request):
    # print('jinlaile')
    if request.POST.get('former') != None:
        username = request.COOKIES.get('username')
        former = request.POST.get('former')
        record = Users.objects.filter(username=username, password=former)
        if record:
            return HttpResponse('认证成功')
        else:
            return HttpResponse('密码错误')
    return HttpResponseRedirect('404')


def change_password_op(request):
    if request.POST.get('latest') != None:
        username = request.COOKIES.get('username')
        latest = request.POST.get('latest')
        Users.objects.filter(username=username).update(password=latest)
        return HttpResponse('success')
    return HttpResponseRedirect('404')


def test(request):
    return render(request, 'test_download.html')


def send_email(request):
    # send_mail('Subject here', 'Here is the message.', '492195925@qq.com',
    #           ['553105821@qq.com'], fail_silently=False)


    subject = '来自西西的问候'

    text_content = '!!!.'

    html_content = '<p>这是一封<strong>重要的</strong>邮件.</p>'

    msg = EmailMultiAlternatives(subject, text_content, '492195925@qq.com', ['492195925@qq.com'])
    # 553105821
    # msg.attach_alternative(html_content, "text/html")
    file = 'C:\\Users\\HP\\Desktop\\SZU\\middle\\' + '中期报告_黄淦_黄树华_基于深度学习的肌电图、脑电图分析2.doc'
    text = open(file, 'rb').read()
    file_name = os.path.basename(file)
    b = make_header([(file_name, 'utf-8')]).encode('utf-8')
    msg.attach(b, text)

    # msg.attach_file(file)


    msg.send()
    return HttpResponse('成功发送！')


# def send_email(request):
#     subject = request.POST.get('subject', '')
#     message = request.POST.get('message', '')
#     from_email = request.POST.get('from_email', '')
#     if subject and message and from_email:
#         try:
#             send_mail(subject, message, from_email, ['admin@example.com'])
#         except BadHeaderError:
#             return HttpResponse('Invalid header found.')
#         return HttpResponseRedirect('/contact/thanks/')
#     else:
#         # In reality we'd use a form class
#         # to get proper validation errors.
#         return HttpResponse('Make sure all fields are entered and valid.')

def index(request):
    date1 = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    date1 = date1.replace("-","")
    print(date1)
    date = Status.objects.all()[0]
    date2 = str(date.date)
    date2 = date2.replace("-","")
    print(date1<=date2)
    # if date1<=date2:
    #     status = 1
    # else:
    #     status = 0
    # print(status)
    username = request.COOKIES.get('username')
    if ProInfo.objects.filter(leader_id=username):
        status = Status.objects.all()[0]
        mode = status.mode
        date1 = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        date1 = date1.replace("-", "")
        date = Status.objects.all()[0]
        date2 = str(date.date)
        date2 = date2.replace("-", "")
        return render(request, 'base.html', {'username': username, 'status': mode, 'date': date1 <= date2})
    return render(request, 'index.html',{'date':date1 <= date2})


def base_mypro(request):
    username = request.COOKIES.get('username')

    info = []
    if ProInfo.objects.filter(leader_id=username):
        leader = Users.objects.get(username=username)
        pro = ProInfo.objects.filter(leader_id=username)
        for i in pro:
            info1 = model_to_dict(i)
            mem_info = Members.objects.filter(pro_id=i.id)
            memlist = []
            for i in mem_info:
                memlist.append(i.stu_id)
            memlist = '/'.join(memlist)
            info1["pro_mems"] = memlist
            info1["name"] = leader.name
            info.append(info1)
    if Members.objects.filter(stu_id=username):
        print('')
        pro = Members.objects.filter(stu_id=username)
        for i in pro:
            id = i.pro_id
            pro = ProInfo.objects.filter(id=id)
            for i in pro:
                info2 = model_to_dict(i)
                leader = Users.objects.get(username=i.leader_id)
                mem_info = Members.objects.filter(pro_id=i.id)
                memlist = []
                for k in mem_info:
                    memlist.append(k.stu_id)
                memlist = '/'.join(memlist)
                info2["pro_mems"] = memlist
                info2["name"] = leader.name
                info.append(info2)

    return render(request, 'base_mypro.html', {'infolist': info})

def index_mypro(request):
    username = request.COOKIES.get('username')
    info = []
    if ProInfo.objects.filter(leader_id=username):
        leader = Users.objects.get(username=username)
        pro = ProInfo.objects.filter(leader_id=username)
        for i in pro:
            info1 = model_to_dict(i)
            mem_info = Members.objects.filter(pro_id=i.id)
            memlist = []
            for i in mem_info:
                memlist.append(i.stu_id)
            memlist = '/'.join(memlist)
            info1["pro_mems"] = memlist
            info1["name"] = leader.name
            info.append(info1)
    if Members.objects.filter(stu_id=username):
        print('')
        pro = Members.objects.filter(stu_id=username)
        for i in pro:
            id = i.pro_id
            pro = ProInfo.objects.filter(id=id)
            for i in pro:
                info2 = model_to_dict(i)
                leader = Users.objects.get(username=i.leader_id)
                mem_info = Members.objects.filter(pro_id=i.id)
                memlist = []
                for k in mem_info:
                    memlist.append(k.stu_id)
                memlist = '/'.join(memlist)
                info2["pro_mems"] = memlist
                info2["name"] = leader.name
                info.append(info2)

    return render(request, 'index_mypro.html', {'infolist': info})

def apply_model(request):
    if request.COOKIES.get('username', '') != '':
        username = request.COOKIES.get('username')
        user_info = ProInfo.objects.filter(leader_id=username)
        if user_info:
            filename = '申请报告模板.doc'
            path = os.getcwd() + os.sep + 'models'
            file = os.path.join(path, filename)
            return HttpResponse(file.encode('utf-8'))
        return HttpResponseRedirect('/basic')
    return HttpResponseRedirect('/login')


def middle_model(request):
    if request.COOKIES.get('username', '') != '':
        username = request.COOKIES.get('username')
        user_info = ProInfo.objects.filter(leader_id=username)
        if user_info:
            filename = '中期报告模板.doc'
            path = os.getcwd() + os.sep + 'models'
            file = os.path.join(path, filename)
            return HttpResponse(file.encode('utf-8'))
        return HttpResponseRedirect('/basic')
    return HttpResponseRedirect('/login')


def conclusion_model(request):
    if request.COOKIES.get('username', '') != '':
        username = request.COOKIES.get('username')
        user_info = ProInfo.objects.filter(leader_id=username)
        if user_info:
            filename = '结题报告模板.doc'
            path = os.getcwd() + os.sep + 'models'
            file = os.path.join(path, filename)
            return HttpResponse(file.encode('utf-8'))
        return HttpResponseRedirect('/basic')
    return HttpResponseRedirect('/login')

def infostore(request):
    username = request.GET.get('username')
    phone = request.GET.get('leader_phone')
    email = request.GET.get('leader_email')
    pro_name = request.GET.get('pro_name')
    tutor_name = request.GET.get('tutor_name')
    members = request.GET.get('members').strip()
    memlist = members.split("/")
    print(memlist)
    Users.objects.filter(username=username).update(phone=phone, email=email)
    if ProInfo.objects.filter(leader_id=username):
        ProInfo.objects.filter(leader_id=username).update(pro_name=pro_name, tutor_id=tutor_name)
    else:
        ProInfo.objects.create(leader_id=username, pro_name=pro_name, tutor_id=tutor_name)
    pro_object = ProInfo.objects.filter(leader_id=username)
    for i in pro_object:
        pro_id = i.id
        print('pro_id是：' + str(pro_id))
    if Members.objects.filter(pro_id=pro_id):
        Members.objects.filter(pro_id=pro_id).delete()
    for i in memlist:
        Members.objects.create(pro_id=pro_id, stu_id=i)
    if not Middle.objects.filter(leader_id=username):
        print('建立中期报告数据库')
        print(pro_id)
        Middle.objects.create(pro_id=pro_id, leader_id=username)
    if not
    return HttpResponse('success')

def middle(request):
    if request.COOKIES.get('username', '') != '':
        username = request.COOKIES.get('username')
        print(username)
        pro_middle = Middle.objects.filter(leader_id=username)
        for i in pro_middle:
            info = model_to_dict(i)
            pro_id = i.pro_id
        print('项目id' + str(pro_id))
        print(type(i.export_time))
        pro_info = ProInfo.objects.filter(id=pro_id)
        for i in pro_info:
            info['pro_name'] = i.pro_name
            info['tutor_id'] = i.tutor_id
            id = i.id
        mem_info = Members.objects.filter(pro_id=id)
        memlist = []
        for i in mem_info:
            memlist.append(i.stu_id)
        info["pro_mems"] = '/'.join(memlist)
        user_info = Users.objects.filter(username=username)
        for i in user_info:
            info['pro_leader'] = i.name
            info['leader_phone'] = i.phone
        print(info)
        for i in pro_middle:
            print(i.status)
            if i.status == '1':
                return render(request, 'submitted_middle.html', {'info': info})
        return render(request, 'middle.html',
                      {'info': info})
    return HttpResponseRedirect('/login')



def apply(request):
    if request.COOKIES.get('username', '') != '':
        # username = request.COOKIES.get('username')
        # user = Users.objects.filter(username=username)
        # for i in user:
        #     pro_name = i.pro_name
        #     tutor_name = i.tutor_name
        #     name = i.name
        #     sex = i.sex
        #     major = i.major
        #     phone = i.phone
        #     email = i.email
        # return render(request, 'test5.html', {'username': username, 'pro_name': pro_name, 'tutor_name': tutor_name,
        #                                       'pro_leader': name, 'sex': sex, 'major': major, 'leader_phone': phone,
        #                                       'leader_email': email})
        return render(request, 'apply.html')
    return HttpResponseRedirect('/login')
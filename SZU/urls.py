"""SZU URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static

from Innovation import views, admin_op
from SZU import settings

urlpatterns = [
                  # url(r'^admin/', admin.site.urls),
                  url(r'^test', views.test),
                  url(r'^send_email', views.send_email),
                  url(r'^admin/login', admin_op.login),
                  url(r'^admin/check$', admin_op.check),
                  url(r'^admin/welcome', admin_op.admin_welcome),
                  url(r'^admin/infolist', admin_op.manage_info),
                  url(r'^admin/userlist', admin_op.manage_user),
                  url(r'^admin/status', admin_op.manage_status),
                  url(r'^admin/change_status', admin_op.change_status),
                  url(r'^admin/edit_email', admin_op.edit_email),
                  url(r'^admin/save', admin_op.save_user),
                  url(r'^admin/del_user', admin_op.del_name),
                  url(r'^admin/add_user', admin_op.add_name),
                  url(r'^admin/upload/file$', admin_op.getfile),
                  url(r'^admin/userlist_model$', admin_op.userlist_model),
                  url(r'^export$', admin_op.export),
                  # url(r'^apply_operation',views.write_to_application),
                  url(r'^apply$', views.apply),
                  url(r'^apply_model$', views.apply_model),
                  url(r'^middle$', views.middle),
                  url(r'^middle_model$', views.middle_model),
                  # url(r'^middle_operation',views.write_to_middle),
                  url(r'^conclusion_model$', views.conclusion_model),
                  url(r'^middle_save', views.save_middle),
                  url(r'^success', views.success),
                  url(r'^downloadfile', views.downloadFile),
                  url(r'^check$', views.check),
                  url(r'^login', views.login),
                  url(r'^cancel', views.cancel),
                  url(r'^basic', views.basic),
                  url(r'^welcome', views.welcome),
                  url(r'^infostore', views.infostore),
                  url(r'^upload_apply$', views.upload_apply),
                  url(r'^upload/file$', views.getfile),
                  # url(r'^export$',views.export),
                  url(r'^chgpwd$', views.change_password),
                  url(r'^checkpwd$', views.check_password),
                  url(r'^op_chagpwd', views.change_password_op),
                  url(r'^index',views.index),
                  url(r'^mypro',views.mypro),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

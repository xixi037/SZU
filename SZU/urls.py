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

from Innovation import views, admin_op, exportword, reports
from SZU import settings

urlpatterns = [
                  # url(r'^admin/', admin.site.urls),
                  url(r'^test', views.test),
                  url(r'^send_email', views.send_email),
                  url(r'^admin/base$', admin_op.admin_base),
                  url(r'^admin/chgpwd$', admin_op.change_password),
                  url(r'^admin/checkpwd$', admin_op.check_password),
                  url(r'^admin/op_chagpwd', admin_op.change_password_op),
                  url(r'^admin/login', admin_op.login),
                  url(r'^admin/check$', admin_op.check),
                  url(r'^admin/base/apply_infolist', admin_op.manage_apply_info),
                  url(r'^admin/base/middle_infolist', admin_op.manage_middle_info),
                  url(r'^admin/base/conclude_infolist', admin_op.manage_conclude_info),
                  url(r'^admin/base/files_infolist', admin_op.manage_files_info),
                  url(r'^admin/base/userlist', admin_op.manage_user),
                  url(r'^admin/base/status', admin_op.manage_status),
                  url(r'^admin/base/date', admin_op.manage_date),
                  url(r'^admin/change_mode', admin_op.change_mode),
                  url(r'^admin/change_date', admin_op.change_date),
                  url(r'^admin/edit_email', admin_op.edit_email),
                  url(r'^admin/save', admin_op.save_user),
                  url(r'^admin/del_user', admin_op.del_name),
                  url(r'^admin/add_user', admin_op.add_name),
                  url(r'^admin/upload_file$', admin_op.getfile),
                  url(r'^admin/userlist_model$', admin_op.userlist_model),
                  url(r'^admin/write_to_apply$', exportword.write_to_apply),
                  url(r'^admin/write_to_middle$', exportword.write_to_middle),
                  url(r'^admin/write_to_conclude$', exportword.write_to_conclude),
                  url(r'^admin/write_to_files$', exportword.write_to_files),
                  url(r'^apply$', views.apply),
                  url(r'^apply_model$', views.apply_model),
                  url(r'^apply_save$', reports.save_apply),
                  url(r'^middle$', views.middle),
                  url(r'^middle_model$', views.middle_model),
                  url(r'^middle_save$', reports.save_middle),
                  url(r'^conclude$',views.conclude),
                  url(r'^conclude_model$', views.conclude_model),
                  url(r'^conclude_save$', reports.save_conclude),
                  url(r'^success', views.success),
                  url(r'^downloadfile', views.downloadFile),
                  url(r'^check$', views.check),
                  url(r'^login', views.login),
                  url(r'^cancel', views.cancel),
                  url(r'^basic', views.basic),
                  url(r'^infostore', views.infostore),
                  url(r'^upload_apply$', views.upload_apply),
                  url(r'^upload_conclude$', views.upload_conclude),
                  url(r'^upload/file_apply$', views.getfile_apply),
                  url(r'^upload/file_conclude$', views.getfile_conclude),
                  url(r'^chgpwd$', views.change_password),
                  url(r'^checkpwd$', views.check_password),
                  url(r'^op_chagpwd', views.change_password_op),
                  url(r'^index$', views.index),
                  url(r'^base/mypro$', views.base_mypro),
                  url(r'^index/mypro$', views.index_mypro),
                  url(r'^base$', views.base),
                  url(r'^nav_status$', views.nav_status),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

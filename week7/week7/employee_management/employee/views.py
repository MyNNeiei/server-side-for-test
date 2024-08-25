import json
from django.db.models.functions import Concat
from django.db.models import Value,F,Count
from django.shortcuts import render
from django.views import View
from .models import *
from django.http import JsonResponse
# Create your views here.
class IndexView(View):
    def get(self, request):
        employee_fullname = Employee.objects.annotate(fullname = Concat(F('first_name'),Value(' '),F('last_name'))).order_by("id")
        employee_num = employee_fullname.count()
        context = {"num" : employee_num,
                   "fullname" : employee_fullname}
        return render(request, "employee.html", context)

class PositionView(View):
    def get(self, request):
        position_count = Position.objects.annotate(posi_coount = Count("employee")).order_by("id")
        context = {"position_count" : position_count}
        return render(request, "position.html", context)
    
class ProjectView(View):
    def get(self, request):
        project = Project.objects.all()
        context = {"project" : project}
        return render(request, "project.html", context)
    
    def delete(self, request,dele):
        pro_id = Project.objects.get(id=dele)
        pro_id.delete()
        return JsonResponse({'status': 'ok'})

class ProjectDetailView(View):
    def get(self, request, detail):
        project_detail = Project.objects.get(pk=detail)
        all_project = project_detail.staff.all()
        manager = Employee.objects.filter(id = project_detail.manager_id)
        sdate = project_detail.start_date.strftime("%Y-%m-%d")
        ddate = project_detail.due_date.strftime("%Y-%m-%d")
        context = { "project_detail": project_detail,
                   "all_project" : all_project,
                   "sdate" : sdate,
                   "ddate" : ddate,
                   "manager" : manager}
        return render(request, "project_detail.html", context)
        
    def delete(self, request, project_id, emp_id):
        project = Project.objects.get(id=project_id)
        employee = Employee.objects.get(id=emp_id)
        project.staff.remove(employee)
        return JsonResponse({'status': 'ok'})
    
    def put(self, request, project_id, emp_id):
        project = Project.objects.get(id=project_id)
        employee = Employee.objects.get(id=emp_id)
        if employee not in project.staff.all():
            project.staff.add(employee)
        return JsonResponse({'status': 'ok'})
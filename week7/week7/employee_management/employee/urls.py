from django.urls import path
from . import views
urlpatterns = [
    # ex: /polls/
    path("", views.IndexView.as_view(), name="employee"),
    path("position/", views.PositionView.as_view(), name="position"),
    path("project/", views.ProjectView.as_view(), name="project"),
    path("project/<int:detail>", views.ProjectDetailView.as_view(), name="project_detail"),
    path("project/<int:dele>/delete/", views.ProjectView.as_view(), name="project_delete"),
    path("project/<int:project_id>/<int:emp_id>/add/", views.ProjectDetailView.as_view(), name="project_detail_add"),
    path("project/<int:project_id>/<int:emp_id>/remove/", views.ProjectDetailView.as_view(), name="project_detail_remove")
]
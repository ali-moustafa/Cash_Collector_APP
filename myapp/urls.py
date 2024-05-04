from myapp.views.home import home
from django.urls import path

from myapp.views.tasks import TaskView
from myapp.views.employees import EmployeeView

app_name = 'myapp'
urlpatterns = [
    # ex: /myapp/
    path('', home, name='home'),
    path('tasks/all', TaskView.as_view({'get': 'get_all_tasks'})),
    path('tasks/done', TaskView.as_view({'get': 'get_collector_done_tasks'})),
    path('tasks/next', TaskView.as_view({'get': 'get_collector_next_task'})),
    path('tasks/status', TaskView.as_view({'get': 'get_collector_status'})),
    path('tasks/<int:pk>/collect', TaskView.as_view({'patch': 'patch_collect'})),
    path('tasks/<int:pk>/deliver', TaskView.as_view({'patch': 'patch_deliver'})),
    path('employees/', EmployeeView.as_view()),
]

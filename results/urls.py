from django.urls import path
from results.views import add_result, list_results, edit_result

app_name = "results"

urlpatterns = [
    path("", list_results, name="list_results"),
    path("add/", add_result, name="add_result"),
    path("edit/<int:race_id>/<int:result_id>/", edit_result, name="edit_result"),
]

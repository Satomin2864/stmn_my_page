from django.urls import include, path
from . import views
urlpatterns = [
    path("test", views.test_view),
    path("stmn_top_page",views.stmn_top_page)
]
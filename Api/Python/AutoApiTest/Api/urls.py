from django.urls import include, path

from .views import PersonController

urlpatterns = [path('person/',PersonController.as_view()),
            path('person/<int:id>',PersonController.as_view())]

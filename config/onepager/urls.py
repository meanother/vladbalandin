from django.contrib import admin
from django.urls import path, include
from .views import PollQuestionsDetailView, ShortQuestionsDetailView


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('onepage', include('onepager.urls')),
    path(r'short/', ShortQuestionsDetailView.as_view()),
    path(r'full/', PollQuestionsDetailView.as_view()),
]

from django.urls import path
from .views import PollQuestionsDetailView, ShortQuestionsDetailView
from django.urls import path

from .views import PollQuestionsDetailView, ShortQuestionsDetailView, QuizQuestionsDetailView

urlpatterns = [
    path(r'short/', ShortQuestionsDetailView.as_view()),
    path(r'full/', PollQuestionsDetailView.as_view()),
    path(r'quiz/', QuizQuestionsDetailView.as_view()),
]

from django.urls import path
from .views import PollQuestionsDetailView, ShortQuestionsDetailView
from django.urls import path

from .views import PollQuestionsDetailView, ShortQuestionsDetailView

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('onepage', include('onepager.urls')),
    path(r'short/', ShortQuestionsDetailView.as_view()),
    path(r'full/', PollQuestionsDetailView.as_view()),
]

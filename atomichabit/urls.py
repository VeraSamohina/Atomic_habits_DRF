from django.urls import path

from atomichabit.apps import AtomichabitConfig
from atomichabit.views import (HabitCreateAPIView, HabitDetailAPIView,
                               HabitListAPIView, HabitPublicListAPIView)

app_name = AtomichabitConfig.name


urlpatterns = [
    path('create/', HabitCreateAPIView.as_view(), name='habit-create'),
    path('<int:pk>/', HabitDetailAPIView.as_view(), name='habit-retrieve'),
    path('<int:pk>/update/', HabitDetailAPIView.as_view(), name='habit-update'),
    path('<int:pk>/delete/', HabitDetailAPIView.as_view(), name='habit-delete'),
    path('public/', HabitPublicListAPIView.as_view(), name='public-list'),
    path('', HabitListAPIView.as_view(), name='habit-list',)
    ]

from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (
    HabitListCreateAPIView,
    HabitRetrieveUpdateDestroyAPIView,
    PublicHabitListAPIView,
)

app_name = HabitsConfig.name

urlpatterns = [
    path("habits/", HabitListCreateAPIView.as_view(), name="habit-list-create"),
    path("habits/<int:pk>/", HabitRetrieveUpdateDestroyAPIView.as_view(), name="habit-detail"),
    path("habits/public/", PublicHabitListAPIView.as_view(), name="public-habit-list"),
]
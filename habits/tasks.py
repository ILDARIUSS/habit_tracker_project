from celery import shared_task
from django.utils import timezone

from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def send_habit_reminders():
    now = timezone.localtime()

    habits = Habit.objects.filter(time=now.time())

    for habit in habits:
        if habit.owner.telegram_chat_id:
            message = f"Напоминание: {habit.action} в {habit.time}"
            send_telegram_message(habit.owner.telegram_chat_id, message)
from rest_framework.serializers import ValidationError


class HabitValidator:

    def __call__(self, attrs):
        reward = attrs.get("reward")
        related_habit = attrs.get("related_habit")
        is_pleasant = attrs.get("is_pleasant")
        execution_time = attrs.get("execution_time")
        periodicity = attrs.get("periodicity")

        # 1. Нельзя и reward и related_habit
        if reward and related_habit:
            raise ValidationError(
                "Нельзя одновременно указывать вознаграждение и связанную привычку"
            )

        # 2. Время выполнения <= 120 сек
        if execution_time and execution_time > 120:
            raise ValidationError(
                "Время выполнения не должно превышать 120 секунд"
            )

        # 3. Периодичность <= 7 дней
        if periodicity and periodicity > 7:
            raise ValidationError(
                "Нельзя выполнять привычку реже, чем 1 раз в 7 дней"
            )

        # 4. Связанная привычка должна быть приятной
        if related_habit and not related_habit.is_pleasant:
            raise ValidationError(
                "Связанная привычка должна быть приятной"
            )

        # 5. У приятной привычки не может быть reward или related_habit
        if is_pleasant and (reward or related_habit):
            raise ValidationError(
                "У приятной привычки не должно быть вознаграждения или связанной привычки"
            )
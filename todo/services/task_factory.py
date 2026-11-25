from todo.models import Task


class TaskFactory:

    @staticmethod
    def create_task(title):

        title = title.strip()

        if not title:
            raise ValueError(
                "Title cannot be empty."
            )

        return Task.objects.create(
            title=title
        )

from django.test import TestCase

from todo.models import Task


class CompleteTaskTests(TestCase):

    def test_mark_task_complete(self):

        task = Task.objects.create(
            title="Complete Me"
        )

        task.completed = True

        task.save()

        self.assertTrue(
            task.completed
        )

    def test_toggle_completion(self):

        task = Task.objects.create(
            title="Toggle Task"
        )

        task.completed = not task.completed

        task.save()

        self.assertTrue(
            task.completed
        )

from django.test import TestCase

from todo.models import Task


class UpdateTaskTests(TestCase):

    def test_update_task_title(self):

        task = Task.objects.create(
            title="Old Title"
        )

        task.title = "Updated Title"

        task.save()

        updated_task = Task.objects.get(
            id=task.id
        )

        self.assertEqual(
            updated_task.title,
            "Updated Title"
        )

    def test_update_completed_status(self):

        task = Task.objects.create(
            title="Sample Task"
        )

        task.completed = True

        task.save()

        self.assertTrue(
            task.completed
        )

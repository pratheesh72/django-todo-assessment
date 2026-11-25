from django.test import TestCase

from todo.models import Task


class DeleteTaskTests(TestCase):

    def test_delete_task_success(self):

        task = Task.objects.create(
            title="Delete Me"
        )

        task_id = task.id

        task.delete()

        self.assertFalse(
            Task.objects.filter(
                id=task_id
            ).exists()
        )

    def test_delete_reduces_count(self):

        Task.objects.create(
            title="Task One"
        )

        task = Task.objects.first()

        task.delete()

        self.assertEqual(
            Task.objects.count(),
            0
        )

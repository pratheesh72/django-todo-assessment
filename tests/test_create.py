from django.test import TestCase

from todo.models import Task


class CreateTaskTests(TestCase):

    def test_create_task_success(self):

        task = Task.objects.create(
            title="Prepare interview"
        )

        self.assertEqual(
            task.title,
            "Prepare interview"
        )

        self.assertFalse(
            task.completed
        )

    def test_task_count_increases(self):

        initial_count = Task.objects.count()

        Task.objects.create(
            title="New Task"
        )

        self.assertEqual(
            Task.objects.count(),
            initial_count + 1
        )

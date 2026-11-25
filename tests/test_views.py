from django.test import TestCase
from django.urls import reverse

from todo.models import Task


class TaskViewTests(TestCase):

    def test_home_page_loads(self):

        response = self.client.get(
            reverse("index")
        )

        self.assertEqual(
            response.status_code,
            200
        )

    def test_create_task_from_form(self):

        response = self.client.post(
            reverse("index"),
            {"title": "Test Task"}
        )

        self.assertEqual(
            response.status_code,
            302
        )

        self.assertEqual(
            Task.objects.count(),
            1
        )

    def test_complete_task(self):

        task = Task.objects.create(
            title="Task"
        )

        self.client.get(
            reverse(
                "complete",
                args=[task.id]
            )
        )

        task.refresh_from_db()

        self.assertTrue(
            task.completed
        )

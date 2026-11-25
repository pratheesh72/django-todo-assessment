from django.test import TestCase
from todo.models import Task
class T(TestCase):
  def test_create(self): Task.objects.create(title="a"); self.assertEqual(Task.objects.count(),1)

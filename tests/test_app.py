import unittest
from app import tasks

class TestApp(unittest.TestCase):

    def test_get_tasks(self):
        self.assertIsInstance(tasks, list)
        self.assertGreater(len(tasks), 0)

    def test_task_structure(self):
        task = tasks[0]
        self.assertIn("id", task)
        self.assertIn("title", task)
        self.assertIn("done", task)
        self.assertIsInstance(task["done"], bool)

if __name__ == "__main__":
    unittest.main()

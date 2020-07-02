import unittest
from Student_class import Student

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = student.Student('Kilmer, 'Lisa')

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Kilmer')
        self.assertEqual(self.student.first_name, 'Lisa')




if __name__ == '__main__':
    unittest.main()

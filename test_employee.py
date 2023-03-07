import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Mercy', 'Chepu', 10000)
        self.emp_2 = Employee('Emmanuel', 'Korir', 15000)

    def tearDown(self):
        pass    

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Mercy.Chepu@email.com')
        self.assertEqual(self.emp_2.email, 'Emmanuel.Korir@email.com')

        self.emp_1.first = 'Yono'
        self.emp_2.first = 'Meyai'

        self.assertEqual(self.emp_1.email, 'Yono.Chepu@email.com')
        self.assertEqual(self.emp_2.email, 'Meyai.Korir@email.com')
    
        print()

    def test_fullname(self):
        print('test_name ')
        self.assertEqual(self.emp_1.name, 'Mercy Chepu')
        self.assertEqual(self.emp_2.name, 'Emmanuel Korir')

        self.emp_1.first = 'Yono'
        self.emp_2.first = 'Meyai'

        self.assertEqual(self.emp_1.name, 'Yono Chepu')
        self.assertEqual(self.emp_2.name, 'Meyai Korir')

        print()
         
    def test_apply_raise(self):
        print('test_apply_raise ')
        self.emp_1.apply_raise
        self.emp_2.apply_raise

        self.assertEqual(self.emp_1.pay, 10000)
        self.assertEqual(self.emp_2.pay, 15000)

        print()
        

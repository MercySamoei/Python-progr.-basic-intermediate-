import unittest

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

class TestPerson(unittest.TestCase):

    def test_get_name(self):
        person = Person("John", 25)
        self.assertEqual(person.get_name(), "John")

    def test_get_age(self):
        person = Person("John", 25)
        self.assertEqual(person.get_age(), 25)

if __name__ == '__main__':
    unittest.main()
# an example of unit test
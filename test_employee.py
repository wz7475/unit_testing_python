import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setting up')

    @classmethod
    def tearDownClass(cls):
        return super().tearDownClass()

    def setUp(self):
        self.emp1 = Employee('Jan', 'Kowalski', 5000)
        self.emp2 = Employee('Kuba', 'Nowak', 4000)

    def tearDown(self):
        return super().tearDown()

    def test_email(self):
        self.assertEqual(self.emp1.email, 'Jan.Kowalski@email.com')
        self.assertEqual(self.emp2.email, 'Kuba.Nowak@email.com')

        self.emp1.first = 'Janek'
        self.emp2.last = "Nowakowski"

        self.assertEqual(self.emp1.email, 'Janek.Kowalski@email.com')
        self.assertEqual(self.emp2.email, 'Kuba.Nowakowski@email.com')

    def test_apply_raise(self):
        self.assertEqual(self.emp1.pay, 5000)
        self.assertEqual(self.emp2.pay, 4000)

        self.emp1.apply_raise()
        self.emp2.apply_raise()

        self.assertEqual(self.emp1.pay, 1.05*5000)
        self.assertEqual(self.emp2.pay, 1.05*4000)


if __name__ == '__main__':
    unittest.main()

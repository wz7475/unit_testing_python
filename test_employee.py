import unittest
from employee import Employee


class EmployeeTest(unittest.TestCase):

    def test_email(self):
        emp1 = Employee('Jan', 'Kowalski', 5000)
        emp2 = Employee('Kuba', 'Nowak', 4000)

        self.assertEqual(emp1.email, 'Jan.Kowalski@email.com')
        self.assertEqual(emp2.email, 'Kuba.Nowak@email.com')

        emp1.first = 'Janek'
        emp2.last = "Nowakowski"

        self.assertEqual(emp1.email, 'Janek.Kowalski@email.com')
        self.assertEqual(emp2.email, 'Kuba.Nowakowski@email.com')

    def test_apply_raise(self):
        emp1 = Employee('Jan', 'Kowalski', 5000)
        emp2 = Employee('Kuba', 'Nowak', 4000)

        self.assertEqual(emp1.pay, 5000)
        self.assertEqual(emp2.pay, 4000)

        emp1.apply_raise()
        emp2.apply_raise()

        self.assertEqual(emp1.pay, 1.05*5000)
        self.assertEqual(emp2.pay, 1.05*4000)


if __name__ == '__main__':
    unittest.main()

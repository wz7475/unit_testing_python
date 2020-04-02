import unittest
from employee import Employee


class EmployeeTest(unittest.TestCase):

    emp1 = Employee('Jan', 'Kowalski', 5000)
    emp2 = Employee('Kuba', 'Nowak', 4000)
    def test_email(self):


        self.assertEqual(EmployeeTest.emp1.email, 'Jan.Kowalski@email.com')
        self.assertEqual(EmployeeTest.emp2.email, 'Kuba.Nowak@email.com')

        EmployeeTest.emp1.first = 'Janek'
        EmployeeTest.emp2.last = "Nowakowski"

        self.assertEqual(EmployeeTest.emp1.email, 'Janek.Kowalski@email.com')
        self.assertEqual(EmployeeTest.emp2.email, 'Kuba.Nowakowski@email.com')

    def test_apply_raise(self):
        

        self.assertEqual(EmployeeTest.emp1.pay, 5000)
        self.assertEqual(EmployeeTest.emp2.pay, 4000)

        EmployeeTest.emp1.apply_raise()
        EmployeeTest.emp2.apply_raise()

        self.assertEqual(EmployeeTest.emp1.pay, 1.05*5000)
        self.assertEqual(EmployeeTest.emp2.pay, 1.05*4000)


if __name__ == '__main__':
    unittest.main()

import unittest
from calc import calc_me

class CalcTest(unittest.TestCase):
    def test_add(self):
        "Сложение"
        self.assertEqual(calc_me(1, 2,"+"), 3)
        
    def test_sub(self):
        "Вычитание"
        self.assertEqual(calc_me(4, 2,"-"), 2)
        
    def test_mul(self):
        "Умножение"
        self.assertEqual(calc_me(12345679, 8,"*"), 98765432)
        
    def test_div(self):
        "Деление"
        self.assertEqual(calc_me(111111111, 9,"/"), 12345679)

    def test_div_neg(self):
        """Негативный, деление на ноль"""
        self.assertEqual(calc_me(12, 0,"/"), 'ERROR: Divide by zero!')

    def test_param_string(self):
        """Переменные как строка"""
        self.assertEqual(calc_me("1f", 9,"+"), "ERROR: now it is does not supported")
        self.assertEqual(calc_me(1, "3G","+"), "ERROR: now it is does not supported")
        self.assertEqual(calc_me("1f", "3G","+"), "ERROR: now it is does not supported")
        
    def test_param_empty(self):
        """Передача пустых переменных"""
        self.assertEqual(calc_me(None, 9,"+"), "ERROR: send me Number1", "Тест для первой пустой переменной")
        self.assertEqual(calc_me(1,None, "+"), "ERROR: send me Number2", "Тест для второй пустой переменной")
        
    def test_pow(self):
        """Возведение в степень"""
        self.assertEqual(calc_me(2, 2,"^"), 4, "Возведение в положительную степень")
        self.assertEqual(calc_me(4, -1,"^"), 0.25, "Возведение в отрицательну степень")
        self.assertEqual(calc_me(4, 0,"^"), 1, "Возведение в 0 степень")
        self.assertEqual(calc_me(4, 1,"^"), 4, "Возведение в степень = 1")    


if __name__ == '__main__':
    unittest.main(verbosity=2)
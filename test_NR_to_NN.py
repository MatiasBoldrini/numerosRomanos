import unittest
from .numeros_Romanos import *
class PrimerTests(unittest.TestCase):

    def test_1(self):
        resultado = convertir_a_romanos(1)
        self.assertEqual(resultado,"I") 
    def test_2(self): 
        resultado = convertir_a_romanos(2)
        self.assertEqual(resultado,"II")
    def test_3(self): 
        resultado = convertir_a_romanos(3)
        self.assertEqual(resultado,"III")
    def test_4(self): 
        resultado = convertir_a_romanos(4)
        self.assertEqual(resultado,"IV")
    def test_5(self): 
        resultado = convertir_a_romanos(5)
        self.assertEqual(resultado,"V")
    def test_6(self): 
        resultado = convertir_a_romanos(6)
        self.assertEqual(resultado,"VI")
    def test_7(self): 
        resultado = convertir_a_romanos(7)
        self.assertEqual(resultado,"VII")
    def test_8(self): 
        resultado = convertir_a_romanos(8)
        self.assertEqual(resultado,"VIII")
    def test_9(self): 
        resultado = convertir_a_romanos(9)
        self.assertEqual(resultado,"IX")
    def test_10(self): 
        resultado = convertir_a_romanos(10)
        self.assertEqual(resultado,"X")
    def test_12(self): 
        resultado = convertir_a_romanos(12)
        self.assertEqual(resultado,"XII")
    def test_13(self): 
        resultado = convertir_a_romanos(13)
        self.assertEqual(resultado,"XIII")
    def test_15(self): 
        resultado = convertir_a_romanos(15)
        self.assertEqual(resultado,"XV")
    def test_22(self): 
        resultado = convertir_a_romanos(22)
        self.assertEqual(resultado,"XXII")
    def test_25(self): 
        resultado = convertir_a_romanos(25)
        self.assertEqual(resultado,"XXV")
    def test_27(self): 
        resultado = convertir_a_romanos(27)
        self.assertEqual(resultado,"XXVII")
    def test_38(self): 
        resultado = convertir_a_romanos(38)
        self.assertEqual(resultado,"XXXVIII")
    def test_39(self): 
        resultado = convertir_a_romanos(39)
        self.assertEqual(resultado,"XXXIX")
    def test_44(self): 
        resultado = convertir_a_romanos(44)
        self.assertEqual(resultado,"XLIV")
    def test_52(self): 
        resultado = convertir_a_romanos(52)
        self.assertEqual(resultado,"LII")
    def test_55(self): 
        resultado = convertir_a_romanos(55)
        self.assertEqual(resultado,"LV")
    def test_69(self): 
        resultado = convertir_a_romanos(69)
        self.assertEqual(resultado,"LXIX")
    def test_71(self): 
        resultado = convertir_a_romanos(71)
        self.assertEqual(resultado,"LXXI")
    def test_88(self): 
        resultado = convertir_a_romanos(88)
        self.assertEqual(resultado,"LXXXVIII")
    def test_100(self): 
        resultado = convertir_a_romanos(100)
        self.assertEqual(resultado,"C")
    
    def test_155(self): 
        resultado = convertir_a_romanos(155)
        self.assertEqual(resultado,"CLV")
    def test_399(self): 
        resultado = convertir_a_romanos(177)
        self.assertEqual(resultado,"CLXXVII")
    def test_399(self): 
        resultado = convertir_a_romanos(189)
        self.assertEqual(resultado,"CLXXXIX")
    def test_222(self): 
        resultado = convertir_a_romanos(222)
        self.assertEqual(resultado,"CCXXII")
    def test_350(self): 
        resultado = convertir_a_romanos(350)
        self.assertEqual(resultado,"CCCL")
    def test_350(self): 
        resultado = convertir_a_romanos(366)
        self.assertEqual(resultado,"CCCLXVI")
    
    def test_399(self): 
        resultado = convertir_a_romanos(399)
        self.assertEqual(resultado,"CCCXCIX")
        
if __name__ == '__main__':
    unittest.main()
import unittest
import solv_square_equation
 
class CalcTest(unittest.TestCase):
    def test_discriminant(self):
        self.assertEqual(solv_square_equation.discriminant(33, 555, 52), 301161)
        
    def test_solv_square(self):
        self.assertEqual(solv_square_equation.solv_square(33, 555, 52),  (-0.09422155704467369, -16.723960261137144))
    def test_roots(self):
        self.assertEqual(solv_square_equation.roots(301161, 33, 555, 52),  (-0.09422155704467369, -16.723960261137144))
        
if __name__ == '__main__':
    unittest.main()

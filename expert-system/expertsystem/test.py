import unittest
import evalengine

class Testengine(unittest.TestCase):
    
    
    def test_evaluate_returns_true_when_valid_argument(self):
        userfunc1 = "display(1,2)"
        userfunc2 = "display(1)"
        msg1 = {'action': 'getCurrent', 'context': {'base': 'AUD', 'symbols': ['USD', 'GBP']}}
        msg2 = {'action': 'getcurrent', 'created_at': 1568041517, 'context': {'base': 'AFRI', 'symbols': ['USD', 'GBP']}}
        # self.assertEqual(rateconversion.apiextract(current,msg1), 200)
        # self.assertEqual(evalengine.evaluate(userfunc1), )
        # self.assertFalse(evalengine.evaluate(userfunc1))
        self.assertTrue(evalengine.evaluate(userfunc2))
    
    def test_evaluate_returns_false_when_invalid_argument(self):
        userfunc1 = "display(1,2)"
        self.assertFalse(evalengine.evaluate(userfunc1))


if __name__ == '__main__':
    unittest.main()


# userparam = input("Enter parameter as rule defined:") 

# if type(userparam) is str:
#     settype = 1

# finalfunc = userfunc + '(' + userparam + ')'

# print(userparam)
# try:
#     engine.eval(userfunc)
# except:
#     print("function not executed")

# obj.eval("display('Cheers')")
# obj.eval("checkage(30)")
# obj.eval("checkctr(1.2)")
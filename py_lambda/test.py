import unittest,main

class LambdaTestCase(unittest.TestCase):
    def test_if_works(self):
        f=main._def(("hello:str='world'",),"""
    print("Hello,",hello)        
    """)
        f()

if __name__ == "__main__":
    unittest.main()
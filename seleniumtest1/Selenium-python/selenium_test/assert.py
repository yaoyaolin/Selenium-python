#!/usr/bin/python
# -*- coding:UTF-8 -*-
import time, unittest

class Asserttest(unittest.TestCase):
    def test01(self):
        '''判断a=b'''
        a=1
        b=1
        self.assertEqual(a,b)
        print("a")
    def test02(self):
        a = 'hello'
        b = 'hello world'
        self.assertIn(a,b)
        print("b")
    def test03(self):
        a = True
        self.assertTrue(a)
        print("c")
    def test04(self):
        a = "失败案例"
        b = 123
        self.assertEqual(a,b,msg="失败原因：%s != %s"%(a,b))
        #self.assertEqual(a,b)
        print("d")
if __name__ == "__main__":
    unittest.main()


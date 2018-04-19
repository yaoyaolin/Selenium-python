#coding=utf-8
import unittest
#这里需要导入测试文件
import lianxipaixu
import HTMLTestRunner
testunit = unittest.TestSuite()
#将测试用例加入到测试容器(套件)中
testunit.addTest(unittest.makeSuite(lianxipaixu.Baidu))
#baidu.Baidu中的baidu为用例所在的.py文件的名称，Baidu为测试用例集的名称
#定义个报告存放路径，支持相对路径。
filename = "C:\\Users\\Administrator\\PycharmProjects\\mypython\\" + u"测试报告正常" + "result.html"
fp = open(filename, "wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况：')
#执行测试用例
runner.run(testunit)


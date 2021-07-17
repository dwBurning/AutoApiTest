# AutoApiTest
基于python的接口自动化测试框架
Test部分基于yingoja开源的DemoApi优化修改而来
API部分将继续完善，提供基于C#，Go，Java，Python版本的Api服务程序，目的是为了学习接口测试的同学不需要去搭建其他语言的运行环境，顺便我也复习一下这几门语言的基础语法。
## 测试框架结构目录介绍
目录结构介绍如下：
D:\项目\GITHUB\AUTOAPITEST
├─Api		服务端接口目录
│  ├─DotNet		C#版本		
│  ├─Golang		Go版本
│  ├─Java		Java版本
│  └─Python		Python版本
└─Test		自动化测试目录
    │  run.py		启动程序
    ├─config
    │  │  config.ini		配置文件
    │  │  setting.py		       
    ├─helper
    │  │  excelHelper.py		读写Excel
    │  │  requestHelper.py		发送Http请求
    │  │  sendEmailHelper.py	发送邮件	      
    ├─package
    │  │  HTMLTestRunner.py		第三方库包，用于生成html的报告
    ├─report		生成报告 
    │  └─excelReport
    │          PersonAPITestCase.xlsx        
    └─testcase
        │  apiTestCase.py	测试用例
        │  PersonAPITestCase.xlsx
## 特别感谢
https://github.com/yingoja
# from appium import webdriver
# caps = {}
# caps["platformName"] = "Android"
# caps["platformVersion"] = "6.0.1"
# caps["deviceName"] = "127.0.0.1:7555"
# caps["appPackage"] = "com.tencent.mobileqq"
# caps["appActivity"] = ".activity.SplashActivity"
# caps["noReset"] = "true"
#
# driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
# #添加隐式等待
# driver.implicitly_wait(20)
# print('all_sessions',driver.all_sessions)
# print('capabilities',driver.capabilities)
# print('context',driver.context)
# print('current_activity',driver.current_activity)
# print('current_context',driver.current_context)
# print('current_package',driver.current_package)
#
# el1 = driver.find_element_by_accessibility_id("请输入QQ号码或手机或邮箱")
# el1.send_keys("506135307")
# el2 = driver.find_element_by_accessibility_id("密码 安全")
# el2.clear()
# el2.send_keys("RainQAQ999?")
# el3 = driver.find_element_by_accessibility_id("登 录")
# el3.click()
# el4 = driver.find_element_by_id("com.tencent.mobileqq:id/e3u")
# el4.click()
# el5 = driver.find_element_by_accessibility_id("设置")
# el5.click()
# el6 = driver.find_element_by_id("com.tencent.mobileqq:id/account_switch")
# el6.click()
# el7 = driver.find_element_by_accessibility_id("退出当前帐号按钮")
# el7.click()
# el8 = driver.find_element_by_id("com.tencent.mobileqq:id/dialogRightBtn")
# el8.click()
#
# driver.quit()
#
# import os,threading
#
#
#
# cmd = 'node C:\\Users\\Xy\\AppData\\Local\\Programs\\Appium\\resources\\app\\node_modules\\appium\\build\\lib\\main.js -p 4333'
#
# def run(cmd):
#     os.popen(cmd).read()
# th = threading.Thread(target=run, args=(cmd,))
# th.start()
# print(111)
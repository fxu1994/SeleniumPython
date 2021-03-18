from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
class Login():

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("https://mail.163.com/")

    def element_location(self,position_model,element_express):
        element_object = WebDriverWait(self.driver,30).until(lambda x:x.find_element(by=position_model,value=element_express))
        return element_object

    def login(self):
        iframe = (0)
        self.driver.switch_to.frame(iframe)

        self.driver.find_element_by_name("email").clear()
        self.driver.find_element_by_name("email").send_keys("自己的163邮箱,不用输入邮箱后缀")

        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys("邮箱密码")

        self.driver.find_element_by_id("dologin").click()
        self.driver.close()
        return "login success"


if __name__ == '__main__':

    print(Login().login())





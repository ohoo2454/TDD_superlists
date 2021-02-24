import time

from .base import FunctionTest

TEST_EMAIL = 'edith@mockmyid.com'


class LoginTest(FunctionTest):

    def test_login_with_persona(self):
        
        # 伊迪斯访问这个很棒的超级列表网站
        # 第一次注意到“Sign in”链接
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_login').click()

        # 出现一个Persona登陆框
        self.switch_to_new_window('Mozilla Persona')

        # 伊迪斯使用她的电子邮件地址登陆
        ## 测试中的电子邮件地址使用mockmyid.com
        self.browser.find_element_by_id(
            'authentication_email'
        ).send_keys(TEST_EMAIL)
        self.browser.find_element_by_tag_name('button').click()

        # Persona窗口关闭
        self.switch_to_new_window('To-Do')

        # 她发现自己已经登录
        self.wait_to_be_logged_in(email=TEST_EMAIL)

        # 刷新页面，她发现真的通过会话登录了
        # 而且并不只在那个页面中有效
        self.browser.refresh()
        self.wait_to_be_logged_in(email=TEST_EMAIL)

        # 对这项新功能有些恐惧，她立马点击了退出按钮
        self.browser.find_element_by_id('id_logout').click()
        self.wait_to_be_logged_out(email=TEST_EMAIL)
        
        # 刷新后仍旧保持退出状态
        self.browser.refresh()
        self.wait_to_be_logged_out(email=TEST_EMAIL)

    def switch_to_new_window(self, text_in_title):
        
        retries = 60
        while retries > 0:
            for handle in self.browser.window_handles:
                self.browser.switch_to_window(handle)
                if text_in_title in self.browser.title:
                    return
            retries -= 1
            time.sleep(0.5)
        self.fail('could not find window')

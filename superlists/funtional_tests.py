

import unittest
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get("http://localhost:8000")
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        # 应用邀请他输入一个代办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                         'Enter a to-do item'
                         )
        # 在文本框输入了“Buy peacock feathers”
        # 伊迪斯的爱好是使用假蝇做鱼饵钓鱼
        inputbox.send_keys('Buy peacock feathers')
        # 按下回车键后页面更新
        # 待办事项表格显示了“1：Buy peacock feathers”
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == "1：Buy peacock feathers" for row in rows))
        # 页面显示一个文本框，可以输入其他的待办事项
        # 她输入了“User peacock feathers to make a fly”
        # 伊利斯做事很有调理
        self.fail("Finish the test!")
        # 页面再次更新，她的清单显示了这两个待办事项
        [...]


if __name__ == '__main__':
    unittest.main()





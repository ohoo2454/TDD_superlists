from .base import FunctionTest


class LayoutAndStylingTest(FunctionTest):

    def test_layout_and_styling(self):

        # 伊迪斯访问首页
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        # 她看到输入框完美的居中显示
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            input_box.location['x'] + input_box.size['width'] / 2, 
            512, 
            delta=10
        )

        # 她新建了一个清单，看到输入框仍完美居中显示
        input_box.send_keys('testing\n')
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            input_box.location['x'] + input_box.size['width'] / 2, 
            512, 
            delta=10
        )

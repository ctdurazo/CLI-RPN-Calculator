from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
Config.set('graphics', 'width', '350')
Config.set('graphics', 'height', '500')

import rpn


nums = []


class CalcGridLayout(GridLayout):
    def clear(self):
        global nums
        nums = []
        self.display.text = ""

    def calculate(self, calculation):
        if calculation:
            try:
                rpn.calculator(calculation, nums)
                self.display.text = str(nums[-1])
            except Exception:
                self.display.text = "Error"


class RPNCalculatorApp(App):
    def build(self):
        return CalcGridLayout()


RPNCalculatorApp().run()

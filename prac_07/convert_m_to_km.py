"""
CP1404/CP5632 Practical
Kivy GUI program to convert Miles to Kilometers
Jordan Mellish, IT@JCU
Started 1/10/2018
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Jordan Mellish'


class MilesConversionApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (300, 200)
        self.title = "Conversion - Miles to Kilometres"
        self.root = Builder.load_file('convert_m_to_km.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            result = int(value) * 1.61
        except ValueError:
            result = 0.0
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, number):
        value = (int(self.root.ids.input_number.text) + number)
        self.root.ids.input_number.text = str(value)


MilesConversionApp().run()

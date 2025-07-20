from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

Builder.load_file("..\\gui\\main.kv")

class Backend(Widget):
    pass


class JetCalcApp(App):
    def build(self):
        return Backend()

if __name__ == "__main__":
    JetCalcApp().run()
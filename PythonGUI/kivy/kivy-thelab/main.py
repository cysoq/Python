from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.properties import ObjectProperty
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.switch import Switch
from kivy.uix.progressbar import ProgressBar
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.actionbar import ActionBar
from navigation_screen_manager import NavigationScreenManager
from kivy.uix.tabbedpanel import TabbedPanel
from canvas_examples import *


class MyScreenManager(NavigationScreenManager):
    pass

class TheLabApp(App):
    manager= ObjectProperty(None)
    def build(self):
        self.manager = MyScreenManager()
        return self.manager


TheLabApp().run()

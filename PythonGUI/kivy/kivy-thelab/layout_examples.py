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
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.switch import Switch
from kivy.uix.progressbar import ProgressBar
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel

Builder.load_file("layout_examples.kv")

class StackLayoutExample(StackLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #self.orientation= "rl-tb"
        for i in range(0,100):
            #size = dp(100) + i*10
            b = Button(text=str(i+1), size_hint=(None, None), size=(dp(100), dp(100)))
            self.add_widget(b)
        
# class GridLayoutExample(GridLayout): (Dont need this if you use the @GridLayout on the.kv)
#     pass

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    pass
# See example of how you can add things without a .kv
    """    def __init__(self,**kwargs):
            super().__init__(**kwargs)
            self.orientation = "vertical"
            b1 = Button(text="A")
            b2 = Button(text="B")
            b3 = Button(text="C")
            self.add_widget(b1)
            self.add_widget(b2)
            self.add_widget(b3) """

class mainWidget(Widget):
    pass
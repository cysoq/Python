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

Builder.load_file("widget_examples.kv")

class WidgetsExample(GridLayout):
    count = 1
    my_text = StringProperty("Count!")
    count_enabled = BooleanProperty(False)
    #slider_value_txt = StringProperty("Value")
    text_input_str = StringProperty("foo")
    
    def on_button_click(self):
        if self.count_enabled:
            self.count += 1
            self.my_text = str(self.count)
        
    def on_toggle_button_state(self, widget):
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enabled = False
        else:
             widget.text = "ON"
             self.count_enabled = True
             
    def on_switch_active(self, widget):
        print("Switch: " + str(widget.active))
        
    def on_slider_value(self,widget):
        #print("slider: "+ str(widget.value)) # normally a float, can change to an int
        #self.slider_value_txt = str(int(widget.value))
        pass
    
    def on_text_validate(self, widget):
        self.text_input_str = widget.text
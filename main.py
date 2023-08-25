from kivy.properties import NumericProperty
from kivy.uix.widget import Widget


class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)
    
    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        print("INIT W: " + str(self.width) + " H:" + str(self.height))
    def on_parent(self, widget, parent):
        print("ON PARENT W:" + str(self.width) + " H:" + str(self.height))
        
class TheLabApp():
    pass    


TheLabApp().run()

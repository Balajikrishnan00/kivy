from kivy.app import App
from kivy.lang import Builder
kv="""
BoxLayout:
    size_hint:(1,1)
    ScrollView:
        
        BoxLayout:
            id:container
            orientation:'vertical'
            size_hint_y:None
            height:self.minimum_height
            
            Label:
                size_hint:(1,None)
                height:300
                markup:True
                text:'Sri Rama Jayam'
            Label:
                size_hint: (1, None)
                height: 300
                markup: True
                text: "[size=78]GeeksForGeeks[/size]"
            Label:
                size_hint: (1, None)
                height: 300
                markup: True
                text: "[size=78]GeeksForGeeks[/size]"
            Label:
                size_hint: (1, None)
                height: 300
                markup: True
                text: "[size=78]GeeksForGeeks[/size]"
        
"""
class uiApp(App):
    def build(self):
        return Builder.load_string(kv)
uiApp().run()

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.base import Builder
from kivy.base import runTouchApp
from kivy.app import App
Builder.load_string('''

<BoxLayout>:
    orientation:'vertical'
    padding:20,10
    
    Button:
        background_color:(1,2,3,1)    
        text:'Button 1'
        
        
    Button:
        text:'Button 2'
        
''')
class mylist(BoxLayout):
    pass

if __name__ == '__main__':
    runTouchApp(mylist())


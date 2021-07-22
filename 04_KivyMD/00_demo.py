"""
class hello:
    no1=10

    def bye(self):
        self.no1+=10
        print(self.no1)
    def hi(self):
        self.no1-=10
        print(self.no1)
h=hello()
h.bye()
h.hi()
---------------------------------"""
from kivy.uix.togglebutton import ToggleButton

h=dir(ToggleButton)
#print(ToggleButton.height)
#print(ToggleButton.valign)
#for x in h:
#    print(ToggleButton.x)
#    help(ToggleButton.x)
#help(type(ToggleButton))
from kivy import properties as P

print(dir(P))
help(P)


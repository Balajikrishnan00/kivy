from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.accordion import Accordion,AccordionItem
from kivy.uix.button import Button
class MyApp(App):
    def build(self):
        a1=Accordion()
        a1.orientation='vertical'
        for x in range(5):
            i=AccordionItem(title='Title %d'%x)
            i.add_widget(Label(text='Label %i' % x))

            a1.add_widget(i)

        return a1


if __name__ == '__main__':
    MyApp().run()

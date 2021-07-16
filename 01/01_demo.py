from kivy.uix.label import Label
l=dir(Label)
for i in l:
	if not i.startswith('__'):
		print(i)
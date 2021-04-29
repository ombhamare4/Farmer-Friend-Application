from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.picker import MDDatePicker, MDTimePicker
from kivy.core.window import Window
Builder.load_file('libscreen.kv')
Builder.load_file('appoit1.kv')


class AppoitmentScreen(Screen):
    pass


class libScreen(Screen):
    pass


class wheatScreen(Screen):
    pass


class riceScreen(Screen):
    pass


class jowerScreen(Screen):
    pass


class juteScreen(Screen):
    pass


class maizeScreen(Screen):
    pass


class groundNutScreen(Screen):
    pass


class soyabeanScreen(Screen):
    pass


class cottonScreen(Screen):
    pass


class mangoScreen(Screen):
    pass


class bananaScreen(Screen):
    pass


class grapeScreen(Screen):
    pass


class orangeScreen(Screen):
    pass


class libMenu(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        Window.size = (411, 823)
        sm = ScreenManager()

        sm.add_widget(libScreen(name='lib'))
        sm.add_widget(AppoitmentScreen(name='appoit'))

        sm.add_widget(wheatScreen(name='wheat'))
        sm.add_widget(riceScreen(name='rice'))
        sm.add_widget(jowerScreen(name='jower'))
        sm.add_widget(juteScreen(name='jute'))
        sm.add_widget(maizeScreen(name='maize'))
        sm.add_widget(groundNutScreen(name='groundNut'))
        sm.add_widget(cottonScreen(name='cotton'))
        sm.add_widget(soyabeanScreen(name='soyabean'))
        sm.add_widget(mangoScreen(name='mango'))
        sm.add_widget(bananaScreen(name='banana'))
        sm.add_widget(grapeScreen(name='grape'))
        sm.add_widget(orangeScreen(name='orange'))

        return sm

    def show_date_picker(self):
        datepick = MDDatePicker(callback=self.got_date)
        datepick.open()

    def got_date(self, the_date):
        print(the_date)

    def show_time_picker(self):
        timePick = MDTimePicker()
        timePick.bind(time=self.got_time)
        timePick.open()

    def got_time(self, picker_widget, time):
        print(time)


if __name__ == '__main__':
    libMenu().run()

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import sqlite3
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.picker import MDDatePicker, MDTimePicker,MDThemePicker

Builder.load_file('logReg.kv')
Builder.load_file('menu.kv')
Builder.load_file('appointment.kv')
Builder.load_file('libmenuAndroid.kv')
Builder.load_file('msp.kv')
Builder.load_file('rules.kv')


connection = sqlite3.connect('store_appointments.db')
cursor = connection.cursor()
connection.execute('''CREATE TABLE IF NOT EXISTS userData
         (
         name           TEXT    NOT NULL,
         email            TEXT     NOT NULL,
         password        TEXT NOT NULL
         );''')

connection.execute('''CREATE TABLE IF NOT EXISTS newappoitments
         (
         name           TEXT    NOT NULL,
         email            TEXT     NOT NULL,
         phone         INT NOT NULL,
         visit        CHAR(50));''')


connection.commit()




class LogScreen(Screen):
    def user_log(self):
        log_email=self.ids.email_log.text
        log_password=self.ids.password_log.text

        find_user=("SELECT email FROM userData WHERE email=? and password=?")

        cursor.execute(find_user,[(log_email),(log_password)])
        log_result=cursor.fetchall()
        
        if log_result:
            # for i in log_result:
            #     print("Welcome: "+i[0])
            self.manager.current='menu'
            return("exit")
        else:
            print("Not Account")
        connection.commit()
    pass


class registerScreen(Screen):
    dialog = None
    scr_mngr = ObjectProperty(None)
    def user_reg(self):
        username_register = self.ids.username_reg.text
        email_register=self.ids.email_reg.text
        password_register=self.ids.password_reg.text


        cursor.execute("INSERT INTO userData values(?,?,?)",(username_register,email_register,password_register))
        if not self.dialog:
            self.dialog = MDDialog(
            text="Register Successful",
            
            buttons=[
                 MDFlatButton(
                        text="Ok",
                        # text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialog
                    ),
            ],
        )
        self.dialog.open()
        connection.commit()

    def close_dialog(self, obj):
        self.dialog.dismiss()
    pass



class AppoitmentScreen(Screen):
    dialog = None
    def store_appointments(self):
        appoit_name1 = self.ids.appoit_name.text
        appoit_email1 = self.ids.appoit_email.text
        appoit_number1 = self.ids.appoit_number.text
        appoit_vist1 = self.ids.appoit_vist.text
        cursor.execute("insert into newappoitments values(?,?,?,?)",(appoit_name1, appoit_email1, appoit_number1, appoit_vist1))
        mycursor=cursor.execute("Select * from newappoitments")
        mycursor1=mycursor.fetchall()
        for row in mycursor1:
            print(row)
        connection.commit()
    pass

class MspPrice(Screen):
    dialog = None

    def wheat_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Prices  (Rs/Quintal)", text="Msp : 1975    Mandi : 1975", size_hint=(0.75, 1),
                buttons=[
                    MDFlatButton(text="BACK", on_release=self.close_dialog)])
        self.dialog.open()

    def paddy_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Prices  (Rs/Quintal)", text="Msp : 1868     Mandi : 1850", size_hint=(0.75, 1),
                buttons=[
                    MDFlatButton(text="BACK", on_release=self.close_dialog)])
        self.dialog.open()

    def bajra_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Prices  (Rs/Quintal)", text="Msp : 2150     Mandi : 2200", size_hint=(0.75, 1),
                buttons=[
                    MDFlatButton(text="BACK", on_release=self.close_dialog)])
        self.dialog.open()

    def barley_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Prices  (Rs/Quintal)", text="Msp : 1600     Mandi : 1650", size_hint=(0.75, 1),
                buttons=[
                    MDFlatButton(text="BACK", on_release=self.close_dialog)])
        self.dialog.open()

    def jowar_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Prices  (Rs/Quintal)", text="Msp : 2620     Mandi : 2500", size_hint=(0.75, 1),
                buttons=[
                    MDFlatButton(text="BACK", on_release=self.close_dialog)])
        self.dialog.open()

    def maize_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Prices  (Rs/Quintal)", text="Msp : 1850     Mandi : 1932", size_hint=(0.75, 1),
                buttons=[
                    MDFlatButton(text="BACK", on_release=self.close_dialog)])
        self.dialog.open()

    def ragi_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Prices  (Rs/Quintal)", text="Msp : 3295     Mandi : 3400", size_hint=(0.75, 1),
                buttons=[
                    MDFlatButton(text="BACK", on_release=self.close_dialog)])
        self.dialog.open()

    def tur_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Prices  (Rs/Quintal)", text="Msp : 6000     Mandi : 6050", size_hint=(0.75, 1),
                buttons=[
                    MDFlatButton(text="BACK", on_release=self.close_dialog)])
        self.dialog.open()

    def moong_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Prices  (Rs/Quintal)", text="Msp : 7196     Mandi : 7250", size_hint=(0.75, 1),
                buttons=[
                    MDFlatButton(text="BACK", on_release=self.close_dialog)])
        self.dialog.open()

    def urad_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Prices  (Rs/Quintal)", text="Msp : 6000     Mandi : 6048", size_hint=(0.75, 1),
                buttons=[
                    MDFlatButton(text="BACK", on_release=self.close_dialog)])
        self.dialog.open()

    def cotton_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Prices  (Rs/Quintal)", text="Msp : 5515     Mandi : 5800", size_hint=(0.75, 1),
                buttons=[
                    MDFlatButton(text="BACK", on_release=self.close_dialog)])
        self.dialog.open()

    def groundnut_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Prices  (Rs/Quintal)", text="Msp : 5275     Mandi : 5000", size_hint=(0.75, 1),
                buttons=[
                    MDFlatButton(text="BACK", on_release=self.close_dialog)])
        self.dialog.open()

    def sunflower_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Prices  (Rs/Quintal)", text="Msp : 5885     Mandi : 5900", size_hint=(0.75, 1),
                buttons=[
                    MDFlatButton(text="BACK", on_release=self.close_dialog)])
        self.dialog.open()

    def soyabean_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Prices  (Rs/Quintal)", text="Msp : 3880     Mandi : 3880", size_hint=(0.75, 1),
                buttons=[
                    MDFlatButton(text="BACK", on_release=self.close_dialog)])
        self.dialog.open()

    def sesamum_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Prices  (Rs/Quintal)", text="Msp : 6855     Mandi : 6860", size_hint=(0.75, 1),
                buttons=[
                    MDFlatButton(text="BACK", on_release=self.close_dialog)])
        self.dialog.open()

    def gram_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Prices  (Rs/Quintal)", text="Msp : 5100     Mandi : 5200", size_hint=(0.75, 1),
                buttons=[
                    MDFlatButton(text="BACK", on_release=self.close_dialog)])
        self.dialog.open()

    def masur_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Prices  (Rs/Quintal)", text="Msp : 5100     Mandi : 5100", size_hint=(0.75, 1),
                buttons=[
                    MDFlatButton(text="BACK", on_release=self.close_dialog)])
        self.dialog.open()

    def mustard_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Prices  (Rs/Quintal)", text="Msp : 4650     Mandi : 4500", size_hint=(0.75, 1),
                buttons=[
                    MDFlatButton(text="BACK", on_release=self.close_dialog)])
        self.dialog.open()

    def copra_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Prices  (Rs/Quintal)", text="Msp : 9960     Mandi : 10000", size_hint=(0.75, 1),
                buttons=[
                    MDFlatButton(text="BACK", on_release=self.close_dialog)])
        self.dialog.open()

    def jute_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Prices  (Rs/Quintal)", text="Msp : 4225     Mandi : 4275", size_hint=(0.75, 1),
                buttons=[
                    MDFlatButton(text="BACK", on_release=self.close_dialog)])
        self.dialog.open()

    def coconut_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Prices  (Rs/Quintal)", text="Msp : 2700     Mandi : 2800", size_hint=(0.75, 1),
                buttons=[
                    MDFlatButton(text="BACK", on_release=self.close_dialog)])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    pass

class MainMenu(Screen):
    
    dialog = None
    scr_mngr = ObjectProperty(None)
    def comming_soon(self):
        if not self.dialog:
                self.dialog = MDDialog(
                title="Coming Soon...",
                text="This feature is under devlopment",
                
                buttons=[
                    MDFlatButton(
                            text="Ok",
                            # text_color=self.theme_cls.primary_color,
                            on_release=self.close_dialog
                        ),
                ],
            )
        self.dialog.open()

    def close_dialog(self, obj):
            self.dialog.dismiss()
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


class RulesScreen(Screen):
    pass

class AwardsForFarmerScreen(Screen):
    pass

class CropsrelatedScreen(Screen):
    pass

class FisheriesRelatedScreen(Screen):
    pass

class LivestockandpoultryrelatedScreen(Screen):
    pass

class PolicypapersScreen(Screen):
    pass

class RuralemploymentrelatedScreen(Screen):
    pass

class UsefullResourcesScreen(Screen):
    pass



class AgriApp(MDApp):

    def build(self):
        sm = ScreenManager()
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "500" 
        self.theme_cls.theme_style = "Light" 
        # self.theme_cls.primary_palette = "Blue"
        sm.add_widget(LogScreen(name="log"))
        sm.add_widget(registerScreen(name="reg"))
        sm.add_widget(MainMenu(name='menu'))
        sm.add_widget(AppoitmentScreen(name='appoit'))
        sm.add_widget(libScreen(name='lib'))
        sm.add_widget(MspPrice(name='msp'))

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
        
        sm.add_widget(RulesScreen(name="Rules"))
        sm.add_widget(AwardsForFarmerScreen(name="AFF"))
        sm.add_widget(CropsrelatedScreen(name="croprel"))
        sm.add_widget(FisheriesRelatedScreen(name="fishrel"))
        sm.add_widget(LivestockandpoultryrelatedScreen(name="lpr"))
        sm.add_widget(PolicypapersScreen(name="polpaper"))
        sm.add_widget(RuralemploymentrelatedScreen(name="eulRmpRel"))
        sm.add_widget(UsefullResourcesScreen(name="usRes"))
        return sm

    def show_date_picker(self):
        datepick = MDDatePicker(callback=self.got_date)
        datepick.open()

    def got_date(self, the_date):
        self.store_data(the_date, self)
        pass
        # print(the_date)

    def show_time_picker(self):
        timePick = MDTimePicker()
        timePick.bind(time=self.got_time)
        timePick.open()

    def got_time(self, picker_widget, time):
        return self.store_data(time, self)
        pass

    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()

AgriApp().run()
class BATTARYPHON:
    def __init__(self,phon_model):
     self.phon_model=phon_model
     self.battery_level=100
    def use_app(self,drain_amount):
        self.drain_amount=drain_amount
        self.battery_level=self.battery_level - drain_amount
        print("App used successfully. ")
        if self.battery_level==0:
            print("Battery empty! ")
    def charge_phone(self,charge_amount):
        self.battery_level=self.battery_level + charge_amount
        print("Phon is charging " + str(self.battery_level))
    def show_status(self):
        print("The model phon is : " + self.phon_model , "Battery status is :" + str(self.battery_level) ," %")
class GAMINGPHONE(BATTARYPHON):
    def turbo_mode(self):
        print("Turbo mode activated! High perfoemance is ON!")
phone_name=input("Enter phone mpdel :")
my_phone=GAMINGPHONE(phone_name)
while True:
    chose=input("Enter your chose")
    if chose=='1':
        my_phon=int(input("Enter status used :"))
        my_phone.use_app(my_phon)
    elif chose=='2':
        my_pho=int(input("Enter charger amount :"))
        my_phone.charge_phone(my_pho)
    elif chose=='3':
        my_phone.show_status()
    elif chose =='4':
        my_phone.turbo_mode()
    elif chose=='5' :
        print("Baayyy!")
        break        
    
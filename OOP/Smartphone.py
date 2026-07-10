class Smartphone:
    def __init__(self,model,battery):
        self.model=model
        self.battery=battery
    def show_statue(self):
        print("This phon is "+ self.model ,"|Battery is " + str(self.battery))
    def use_phon(self,amount):
        self.battery=self.battery - amount
        print("This phon was used")
my_phon=Smartphone("iphone 15",100)
my_phon.show_statue()
my_phon.use_phon(20)
my_phon.show_statue()

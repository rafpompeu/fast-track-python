
class Conta():
    def __init__(self,name,id,balance):
        self.name = name
        self.id = id
        self.balance = balance
        self.extract_list = []

    def trasnfer(self, value):
        self.balance-=value
        self.extract_list.append(['trasnfer', value])

    def deposit(self,value):
        self.balance+=value
        self.extract_list.append(['deposit', value])

    def extract(self):
        print(self.extract_list)

        

    def painel(self):
        print("######################")
        print("## Nome:", self.name,"##")
        print("## Id:", self.id,"##")
        print("## balance:", self.balance,"##")
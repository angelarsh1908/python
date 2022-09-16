from unicodedata import name


class programmer:
        company="Microsoft"
        def __init__(self,name,product):
                self.name = name
                self.product=product

        def getdata(self):
            print(f"The name of the programmer {self.company} and the product {self.product} ")

Harsh=programmer("Harsh","SAP")
Alka=programmer('Alka','python')
Harsh.getdata()
Alka.getdata()


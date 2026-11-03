class computer:
    brand = "apple"

    def __init__(self, cpu, ram, ssd):
        print("init method is called")
        self.cpu = cpu
        self.ram = ram
        self.ssd = ssd

    def config(self):
        print("CPU:" ,self.cpu, "RAM:" ,self.ram, "SSD:" ,self.ssd)
    
    @classmethod
    def info(cls):
        return cls.brand
    
    @staticmethod
    def gb_to_bytes(gb):
        return gb * (1024 **3)


com1 = computer('i5', "16GB", "512GB")
com2 = computer('i7', "32GB", "1TB")

print(computer.gb_to_bytes(16))
print(computer.info())
com1.config()
com2.config()
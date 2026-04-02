from pydantic import BaseModel
# making classes using pydantic
class Laptop(BaseModel):
    brand: str
    cpu: str
    gpu: str
    ram: int
myPc = Laptop(
    brand= "tuplar monster",
    cpu="i7-12700h",
    gpu="nvidia 3060",
    ram=32
)
print(myPc.brand)
# making classes the normal way

class Computer:
    def __init__(self, brand, cpu, gpu, ram):
        self.brand = brand
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram
myDesktop = Computer("tuplar monster", "i7-12700h", "nvidia 3060", "32")
print(myDesktop.gpu)
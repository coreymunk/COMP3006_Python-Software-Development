# %%
from autompg import *

auto1 = AutoMPG("Subaru","Impreza",2001,23.0)
auto2 = AutoMPG("Toyota","Supra",1998,19.0)
auto3 = AutoMPG("Toyota","Tacoma",1998,19.0)

# print(auto1)
# print(auto2)

# print(auto2.make == auto3.make)
# print(auto1.make == auto2.make)

print(auto2.make < auto3.make)
# print(auto1.year < auto2.year)

# hash(auto1.make)

# %%

from address import Address
from mailing import Mailing

to_address = Address ("673354","Улан-Удэ", "Ленина", "32","34")
from_address = Address ("673354","Улан-Удэ", "Ленина", "32","34")

mailing = Mailing ( to_address, from_address, 244, "EFA456567")

print(mailing)


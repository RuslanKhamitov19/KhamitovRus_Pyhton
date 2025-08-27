from address import Address
from mailing import Mailing

to_address = Address("148734", "Париж", "Ленина", "123", "34")

from_address = Address("456728", "Краснодар", "Набережная", "12", "111")

MAiling = Mailing("75463597", to_address, from_address, "1299")

print(MAiling)

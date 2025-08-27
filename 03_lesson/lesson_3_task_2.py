from smartphone import Smartphone

catalog =[
        Smartphone (brand="Sony", model="S15", number="+79512353322"),
        Smartphone (brand="Samsung", model="S24", number="+79112357654"),
        Smartphone (brand="Apple", model="15", number="+79514375518"),
        Smartphone (brand="Apple", model="12Mini", number="+79049827364"),
        Smartphone (brand="Nokia", model="Pixel 5", number="+79237575831")
]

for Smartphone in catalog:
    print(f"{Smartphone.brand} - {Smartphone.model} - {Smartphone.number}")




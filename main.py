class Address:
    def __init__(self, number, street, city, province):
        self.number = number
        self.street = street
        self.city = city
        self.province = province

    def __str__(self):
        return str(self.number) + "," + self.street + "," + self.city + "," + self.province


class Human:
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address

    def __str__(self):
        return self.name + "\n" + str(self.age) + "\n" + self.gender + "\n" + str(self.address) + "\n"

    def talk(self):
        print(self.name + " is talking...")


def whois(human):
    human.name = "a printed person."


def addAge(age):
    age += 1


address1 = Address(319, "Weldrick RD E", "Richmond Hill", "ON")

yidan = Human("YiDan", 17, "F", address1)
huang = Human("Huang Zheng", 56, "M", Address(15, "Fort York Street", "Toronto", "ON"))

'''
print(yidan.name)
print(yidan.age)
print(yidan.gender)
addr = yidan.address
print(addr.number)
print(addr.street)
print(yidan.address.city)
print(yidan.address.province)
'''
print(yidan)
whois(yidan)
print(yidan)

age = 1
addAge(age)
print(age)
'''
print(huang)
yidan.talk()
huang.talk()

whois(yidan)
whois(huang)
'''

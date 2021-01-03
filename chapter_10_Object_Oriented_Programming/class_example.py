class Phone:
    brand = "Samsung"
    price = 900

    def phone_data(self,a,b):
        print(a+b)
phone_info = Phone()
phone_brand = phone_info.brand
print(phone_brand)
print(phone_info.price)
# call the method
phone_info.phone_data(5,5)

# Author: Deendayal Kumawat
""" Date: 02/03/20
Descriptions: File & IO"""

f = open("poems.txt", "r")
text = f.read()
print(text)
if 'twinkle' in text:
    print(f"Yes twinkle !!!! World found ")
else:
    print("Not Found!!!!!")
f.close()

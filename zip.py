names = ["Adrian", "Bob", "Charlie"]
age = (12,22,33)
city = ["Las Vegas", "Orlando", "Detroit"]

zip_list = zip(names,age,city)

for i in zip_list:
    print(i)

def test_kwargs(**kwargs):
    if "city" in kwargs.keys():
        print("Tem cidade")

test_kwargs()
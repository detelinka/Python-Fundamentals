import re

string = input()

pattern = re.compile(
    r">>(?P<furniture_name>[A-Za-z]+)<<(?P<price>[0-9]+[\.0-9]*)!(?P<quantity>[0-9]+)")

total_money = 0
print("Bought furniture:")
while string != "Purchase":
    result = re.finditer(pattern, string)
    for show in result:
        total_money += float(show["price"]) * float(show["quantity"])
        print(show["furniture_name"])
    string = input()

print(f"Total money spend: {total_money:.2f}")
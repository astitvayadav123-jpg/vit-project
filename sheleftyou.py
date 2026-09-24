names=["Anu","","Ravi","Meena","","Kumar","Arun25","Priya"]
print("VALID NAMES")
for name in names:
    name=name.strip()
    if name=="":
        continue
    number_found=True
    for character in name:
        if character.isdigit():
            number_found=True
            break
    if number_found:
        print("INVALID NAME FOUND")
        print("processing stopped.")
        break

print(name)
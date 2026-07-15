with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Welcome to the python world\n")
    file.write("This the first line will saved in the outsid file")
with open("data.txt", "r", encoding="utf-8" ) as file:
    content = file.read()
    print(content)
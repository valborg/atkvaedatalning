text_array = ["Froskdýr", "Krossfiskar", "Starar", "Lárus"]

def count_as(text_obj):
    lines = text_obj.readlines()
    counter = 0
    for line in lines:
        line = line.lower()
        line = line.replace(".", " ").replace(",", " ").replace("?", " ").replace("!", " ").replace('"', " ").replace("  ", " ")
        for x in range(0,len(line)-2):
            if(line[x] == "e" and line[x+1] in "iy"):
                line = line.replace("{}{}".format(line[x],line[x+1]), "as")
            elif(line[x] == "a" and line[x+1] == "u"):
                line = line.replace("{}{}".format(line[x],line[x+1]), "as")
        for letter in line:
            if (letter in "qwrtpdfghjklzxcbnmðþ"):
                line = line.replace(letter, "s")
            elif(letter in "óíýöáéúæoueyi"):
                line = line.replace(letter, "as")
            elif(letter in "0123456789"):
                line = line.replace(letter, "a")
        counter += line.count("a")
    return counter

for name in text_array:
    with open(name, mode="r", encoding="utf-8") as texti:
        tally = count_as(texti)
        print(tally, name)

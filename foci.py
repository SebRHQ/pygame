def csapatok_beolvasasa(file_name):
    csapatok = []
    with open(file_name, 'r', encoding='utf-8') as file:
        header = file.readline().strip().split(',')
        for line in file:
            data = line.strip().split(',')
            csapat = {}
            for i in range(len(header)):
                csapat[header[i]] = data[i]
            csapatok.append(csapat)
    return csapatok

def csapatok_szama(csapatok):
    return len(csapatok)

def osszes_gol(csapatok):
    ossz_gol = 0
    for csapat in csapatok:
        ossz_gol += int(csapat['rúgott'])
    return ossz_gol

def legtobb_golt_kapott(csapatok):
    legtobb_golt_kapott_csapat = max(csapatok, key=lambda x: int(x['kapott']))
    return legtobb_golt_kapott_csapat['csapat'], int(legtobb_golt_kapott_csapat['kapott'])

def csapatok_rendezese(csapatok):
    return sorted(csapatok, key=lambda x: x['csapat'])

def csapat_pontszam(csapat):
    gyozelmek = int(csapat['győzelem'])
    dontetlenek = int(csapat['döntetlen'])
    return gyozelmek * 3 + dontetlenek

def csapat_golkulonbseg(csapat):
    return int(csapat['rúgott']) - int(csapat['kapott'])

def allas_kiiras(csapatok):
    with open("allas.txt", 'w', encoding='utf-8') as file:
        for csapat in csapatok:
            file.write(f"{csapat['csapat']}: Pontszám - {csapat_pontszam(csapat)}, Gólkülönbség - {csapat_golkulonbseg(csapat)}\n")

# 1. Adatok beolvasása
csapatok = csapatok_beolvasasa("nb1.txt")

# 2. Csapatok száma
print("Csapatok száma:", csapatok_szama(csapatok))

# 3. Összes gól
osszes_golok = osszes_gol(csapatok)
print("Összesen rúgtak gólt:", osszes_golok)

# 4. Legtöbb gólt kapott csapat
legtobb_golt_kapott_csapat, legtobb_golt = legtobb_golt_kapott(csapatok)
print(f"A legtöbb gólt kapott csapat: {legtobb_golt_kapott_csapat}, kapott gólok száma: {legtobb_golt}")

# 5. Csapatok rendezése ABC sorrendbe
csapatok = csapatok_rendezese(csapatok)

# 8. Allás kiírása fájlba
allas_kiiras(csapatok)
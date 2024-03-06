file=open("nb1.txt", "r", encoding="utf-8")
data=[]

row=0
for i in file:
    i=i.strip().split(",")
    if row==0:
        data1=i[0]
        data2=i[1]
        data3=i[2]
        data4=i[3]
        data5=i[4]
        data6=i[5]
    else:
        data.append({data1:i[0], data2:i[1], data3:i[2], data4:i[3], data5:i[4], data6:i[5]})
    row+=1
print("csapatok szama: ",len(data))
golok=0
maxgol=0



for i in data:
    golok+=int(i["rúgott"])
    if int(i["rúgott"])>maxgol:
        maxgol=int(i["rúgott"])

print("osszes gol: ",golok)
for i in data:
    if int(i["rúgott"])==maxgol:
        print("Legtöbb kapás:", i["csapat"], "aki", i["kapott"], "gólt kapott")
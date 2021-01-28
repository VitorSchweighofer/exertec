dna1 = open("C:\\Users\\Usuario\\Desktop\\dna\\vitor.txt", "r")
dna2 = open("C:\\Users\\Usuario\\Desktop\\dna\\vitor2.txt", "r")
dna1_2 = dna1.readline()
dna2_2 = dna2.readline()
def DNA():
    countdif = 0
    for count in range(1000):
        if dna1_2[count] != dna2_2[count]:
            countdif += 1
    print(countdif)
DNA()
#/usr/bin/python3

from itertools import product, groupby



def input_genotype():
    print("Enter Genotypes parents")
    papa = input("father: ")
    mama = input("mother: ")
   
    return papa, mama

def punnett(a, b):

    return [''.join(e)
        for e in product(*([''.join(e) for e in product(*e)]
                    for e in zip(allele(a), allele(b))))]
def allele(e):
    
    return [list(v) for _, v in groupby(e, key = str.lower)]

def check_list(punnett_list):
    
    posibilities = []
    for posible in punnett_list:
        
        row = [posible[i:i+2] for i in range(0, len(posible), 2)]
        
        for i, char in enumerate(row):
            #print(char)
            if char[0] == char[0].lower() and char[1] == char[1].upper():
                low = char[0]
                up = char[1]
                char = up + low
                
                row[i] = char
                #print(row[i])
                #print(row)
        good = ""    
        for i in row:
            good += i
        posibilities.append(good)
        posibilities.sort()
    return posibilities
def filter_list(punnett_list):
    #print(punnett_list)
    pun_dict = {}
    for i, pos in enumerate(punnett_list):
        if pos not in pun_dict.keys():
            pun_dict.update({pos:int(1)})
        else:
            pun_dict[pos] = int(pun_dict[pos]) + 1
    return pun_dict

def calculate_freq(punnett_dict, punnett_list):
    for key in punnett_dict.keys():
        freq = (punnett_dict[key] / len(punnett_list) ) *100
        print("Posibility: {} Frequecy: {}%".format(key, freq))

        
def main():
    papa, mama = input_genotype()
    punnett_list = punnett(papa, mama)
    punnett_list = check_list(punnett_list)
    punnett_dict = filter_list(punnett_list)
    calculate_freq(punnett_dict, punnett_list)

if __name__ == '__main__':
    main()
















"""
My program that can make a global alignment

"""
# METADATA
__author__ = 'Rick Venema'
# IMPORT


def enter_sequences():
    print("Enter the first sequence:")
    seq_1 = input("> ")
    print("Enter the second sequence:")
    seq_2 = input("> ")
    seq_1 = seq_1.upper()
    seq_2 = seq_2.upper()
    return seq_1, seq_2

def scoring():
    match = int(1)
    gap = int(-1)
    mismatch = int(-1)
    return match, gap, mismatch

def calculate(seq_1, seq_2):
    M = []
    
    d = -2
    route = [[]]
    for i in range(len(seq_1)+1):
        M.append([i * d])
    M[0].pop(0)
    for j in range(len(seq_2)+1):
        
        M[0].append(j*d)
    for i in range(len(seq_1)+1):
        if i == 0:
            for j in range(len(seq_2)+1):
                route[0].append('I')
            route[0][0] = 'E'
        else:
            route.append(['D'])
    
    
    for i in range(len(seq_1)): #seq_1 = i
        
        for j in range(len(seq_2)): #seq_2 = j
            DELETE = M[i][j+1] +d
            INSERT = M[i+1][j] +d
            if seq_1[i] == seq_2[j]:
                MATCH = M[i][j] + 1
            else:
                MATCH = M[i][j] -1
            M[i+1].append(max(DELETE, INSERT, MATCH))
            if max(DELETE, INSERT, MATCH) == DELETE:
                route[i+1].append('D')
            elif max(DELETE, INSERT, MATCH) == INSERT:
                route[i+1].append('I')
            else:
                route[i+1].append('M')
           
            
            
    """
    for row in M:
        print(row)
    print("#################")
    for row in route:
        print(row)
    print("#################")
    """
                
    A = seq_1
    B = seq_2
    
    AlignmentA = ""
    AlignmentB = ""
    i = len(A)
    j = len(B)
    
    while i > 0 or j > 0:
        if route[i][j] == 'M':
            AlignmentA = A[i-1] + AlignmentA
            AlignmentB = B[j-1] + AlignmentB
            i = i-1
            j = j-1
        elif route[i][j] == 'I':
            AlignmentA = "-" + AlignmentA
            AlignmentB = B[j-1] + AlignmentB
            j = j-1
            
        elif route[i][j] == 'D':
            AlignmentA = A[i-1] + AlignmentA
            AlignmentB = "-" + AlignmentB
            i = i -1
            
    print("Aligned sequences")
    between = ""
    for i in range(len(AlignmentA)):
        if AlignmentA[i] == AlignmentB[i]:
            between += "|"
        else:
            between += " "
    print(AlignmentA)
    print(between)
    print(AlignmentB)
        
def main():
    seq_1, seq_2 = enter_sequences()
    calculate(seq_1, seq_2)
    
if __name__ == '__main__':
    main()

def p1():
    N = int(input())
    for i in range(N):
        print(str(i + 1) + " Abracadabra")

def p2():
    x = int(input())
    y = int(input())
    if (x > 0 and y > 0):
        print(1)
    elif (x < 0 and y > 0):
        print(2)
    elif (x <0 and y < 0):
        print(3)
    else:
        print(4)
def p3():
    r1, s = [int(x) for x in input().split()]
    j
    r2 = (s << 1) - r1
    print(r2)

def p4():
    input()
    temperatures = [int(x) for x in input().split()]
    count = 0
    for t in temperatures:
        if t < 0:
            count += 1
    print(count)

def p5():
    b = 11
    a = 2
    ans = 1
    for i in range(0, 4):# 0 < i < log(b)
        if ( b & (1 << i)):
            ans *= a
        a *= a
    print(ans)

def p6(): 
    S = input().index('a')
    #id_a = S.index('a')
    #S = S[id_a:]
    print(S)
        
    
def main():
    p6()
        
main()
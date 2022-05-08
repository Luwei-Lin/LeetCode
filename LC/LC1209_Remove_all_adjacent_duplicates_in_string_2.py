def test():
    s = list("deeedbbcccbdaa")
    k = 3
    count = []
    
    n = len(s)
    for i in range(n):
        count.append(0) 
        
    i = 0
    
    for j in range(n):
        s[i] = s[j]
        if i > 0 and s[i - 1] == s[j] :
            count[i] = count[i - 1] + 1
        else:
            count[i] = 1
            
        if count[i] == k:
            i -= k
        i += 1
    print("".join(s[0: i]))
    
def main():
    test()

main()
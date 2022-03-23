#binary lifts things
#chewbacca 
def p1():
    num = int(input())
    #temperatures = [int(x) for x in input().split()]
    complexity = 0
    while num > 0:
        complexity += num % 10
        num /= 10
    print(int(complexity))

def main():
    p1()
main()
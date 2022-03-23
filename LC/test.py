from stack import Stack
def infixToPostfix(expression) -> str:
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = expression.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList) 


class Car:
    def __init__(self, color):
        self.color = color
    def getcolor(self):
        return self.color

class SLinkedListNode:
    def __init__(self, initData, initNext):
        self.data = initData
        self.next = initNext
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self, newData):
        self.data = newData
    def setNext(self, newNext):
        self.next = newNext
class SLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def __str__(self):
        s = "["
        i = 0
        current = self.head
        while current != None:
            if i > 0:
                s = s + ","
            dataObject = current.getData()
            if dataObject != None:
                s = s + dataObject#"%s" % dataObject
                i = i + 1
            current = current.getNext()
        s = s + "]"
        return s
    def add(self, item):
        temp = SLinkedListNode(item, None)
        temp.setNext(self.head)
        self.head = temp
        self.size += 1
    def index(self, item):
        current = self.head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                index = index + 1
        if not found:
            index = -1
        return index
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        self.size -= 1
    def append(self, item):
        temp = SLinkedListNode(item, None)
        if (self.head == None):
            self.head = temp
        else:
            current = self.head
            while (current.getNext() != None):
                current = current.getNext()
            current.setNext(temp)
        self.size += 1
    def pop(self):
        current = self.head
        previous = None
        while (current.getNext() != None): # prevents calling on an empty list
            previous = current
            current = current.getNext()
        if (previous == None):
            self.head = None
        else:
            previous.setNext(None)
        self.size -= 1
        return current.getData()
def test():
    location = SLinkedList()
    location.add("Edmonton")
    location.add("Napa Valley")
    location.append("Vancouver")
    print(location.pop())
    location.add("Boston")
    location.add("Big Sur")
    location.add(27)
    print(location.index("Napa Valley"))
    location.remove(27)
    print(location)

        
def test2():
    sizes = [3, 2, 3, 1, 1]
    s = "descognail"
    sList = list(s)
    res = ""
    if len(sizes) % 2 == 0:#even
        for i in range(0, len(sizes) - 1):
            firstL = sList[i : sizes[i]]
            secondL = sList[sizes[i]: sizes[i] + sizes[i + 1]]
            tempL = secondL + firstL
            print(tempL)
            tempS = "".join(tempL)
            res = res + tempS
    else:#odd
        count = 0
        for i in range(0, len(sizes) - 2, 2):
            firstL = sList[count : count + sizes[i]]
            count += sizes[i]
            secondL = sList[count : count + sizes[i + 1]]
            count += sizes[i+1]
            tempL = secondL + firstL
            tempS = "".join(tempL)
            res = res + tempS
        lastS = "".join(sList[count:])
        res += lastS

        print(res)
def c(n, m):
    if (n - m) <0:
        ans = 0
    else:
        ans = 1 + c((n-m), m)

class Tree:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    

def by_age(tree):
   return tree.age
def by_height(tree):
    return tree.height


def test3():
    rings = "B0R0G0R9R0B0G0"
    count = 0
    pairs = {}
    for i in range(0, 10):
        pairs[str(i)] = []
    colors = ['R', 'G', 'B']
    ringsList = list(rings)
    tempColor = ''
    for c in ringsList:
        if c in colors:
            tempColor = c
        if  '0'<= c <= '9':
            pairs.get(c).append(tempColor)
    for k in pairs.keys():
        tempList = pairs.get(k)
        countB = 0
        countG = 0
        countR = 0
        for e in tempList:
            if e == 'B':
                countB += 1
            elif e == 'G':
                countG += 1
            elif e == 'R':
                countR += 1

        if countB > 0 and countG > 0 and countR > 0:
                count += 1
        
def test4():#time exceeded 
    nums = [4,-2,-3,4,1]
    ans = 0
    subLists = []
    for length in range(2, len(nums) + 1):
        for i in range(0, len(nums)):
            subList = []
            subList.append(nums[i])
            for j in range(i + 1, i + length):
                if j < len(nums):
                    subList.append(nums[j])
                if len(subList) == length:
                    subLists.append(subList)

                
    for lst in subLists:
        lst.sort()
        ans += lst[len(lst) - 1] - lst[0]
    
    print(subLists)        
    print(ans)
        
def test5():#lc2138. Divide a String Into Groups of Size k.
    s = "ctoyjrwtngqwt"
    k = 2
    fill = "n"

    sList = list(s)
    ans = []
    length = 0
    while length < len(s):
        if length + k <= len(s):
            ans.append("".join(sList[length:length + k]))
            length += k
        else:
            temp = "".join(sList[length:len(s)])
            diff = k - (len(s) - length) 
            while diff > 0:
                temp += fill
                diff -= 1
            length += k 
            ans.append(temp)
    print(ans)



def main():
    test5()
main()


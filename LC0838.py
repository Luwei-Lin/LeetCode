class Solution:
    def pushDominoes(self, dominoes) -> str:
        queue = []
        times = []
        dominoes = list(dominoes)
        for i in range (len(dominoes)):#default all times is -1, '.'
            times.append(-1)
            if dominoes[i] != '.':
                queue.append(i)
                times[i] = 0 # times[i] needs to be replace by 0 "first time frame"  bug#1
        while(len(queue) != 0):
            now_p = queue[0]
            queue.pop(0)
            next_p = 0

            if dominoes[now_p] == 'L':# dominoes[now_p] is character instead of now_p #bug 2
                next_p = now_p - 1

            else:
                next_p = now_p + 1

            if(next_p < 0 or next_p >= len(dominoes) or dominoes[now_p] == '.' ):
                continue

            if(dominoes[next_p] == '.'):
                queue.append(next_p)
                dominoes[next_p] = dominoes[now_p]
                times[next_p] = times[now_p] + 1

            elif(times[next_p] == times[now_p] + 1): # when the left and right are in the same tframe
                dominoes[next_p] = '.'
        dominoes = ''.join(dominoes)
        return dominoes
    '''
    Solution2 @lee_215 
    
    '''
    def pushDominoes2(self, d):
        d = 'L' + d + 'R'
        res = ""
        i = 0
        for j in range(1, len(d)):
            if d[j] == '.':
                continue
            middle = j - i - 1
            if i:#i != 0
                res += d[i]
            if d[i] == d[j]:# two characters are the same
                res += d[i] * middle
            elif d[i] == 'L' and d[j] == 'R':#
                res += '.' * middle
            else:
                res += 'R' * int(middle / 2) + '.' * int(middle % 2) + 'L' * int(middle / 2)
            i = j
        return res
    
def main():
    dominoes = ".L.R...LR..L.."
    #dominoes = "R.L"
    print(Solution().pushDominoes(dominoes))


main()
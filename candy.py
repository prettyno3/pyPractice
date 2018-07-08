def candy(self, ratings):
    candynum = [1 for i in range(len(ratings))]
    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i-1]:
            candynum[i] = candynum[i-1] + 1
    for i in range(len(ratings)-2, -1, -1):
        if ratings[i+1] < ratings[i] and candynum[i+1] >= candynum[i]:
            candynum[i] = candynum[i+1] + 1
    return sum(candynum)

def candy2(self, ratings):
    if ratings is None or len(ratings)==0:
        return 0
    res = 1
    pre = 1
    count = 0
    for i in range(1, len(ratings)):
        if ratings[i]>=ratings[i-1]:
            if count>0:
                res+= count*(count+1)/2
                if count>=pre:
                    res+=count-pre+1
                count=0
                pre=1
            if ratings[i]==ratings[i-1]:
                pre=1
            else:
                pre+=1
            res += pre
        else:
            count+=1
    if count>0:
        res+= count*(count+1)/2
        if count>=pre:
            res+=count- pre+1
    return int(res)
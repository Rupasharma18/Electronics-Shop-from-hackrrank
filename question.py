def getMoneySpent(keyboards, drives, b):
    ans=-1
    for x in keyboards:
        for y in drives:
            if x+y<=b:
                ans=max(ans,x+y)
    return(ans)


print getMoneySpent([3,1], [5,2,8], 10)   
print getMoneySpent([4],[5],5)
print getMoneySpent([40,50,60],[6,8,12], 60)
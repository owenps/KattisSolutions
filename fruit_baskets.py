import itertools
def findbaskets(fruits):
    # for n fruit there are 2^n - 1 combinations
    # if a fruit > 200g it will be in total sum 2^n/2 times (everytime it is used)
    # discard sums that are less than 200
    n = len(fruits)
    total = sum(list(map(lambda x: x*(2**(n-1)),fruits)))
    light_fruits = list(filter(lambda x: x<200, fruits))
    total -= sum(light_fruits)
    for l in range(2,min(len(light_fruits)+1,4)):
        for basket in itertools.combinations(light_fruits,l):
            total -= sum(basket) if sum(basket) < 200 else 0
    return total

N = int(input())
fruits = list(map(int,input().split()))
print(findbaskets(fruits))
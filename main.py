'''
Create a function named EVEN that will take 2 int parameters.
one for starting point and the other is a counter.
return a list of counter smallest even int
greater than or equal to starting point in ascending order
'''


def even(start, times):

    numList =[]

    for i in range(start, start+times*2):
        if i%2==0:
            numList.append(i)
    print(numList)

def even2(start, n):
    if start%2 == 0:
        start = start
    else:
        start = start + 1

    newList = []
    i = 0
    while i < n:
        newList.append(start)
        start = start +2
        i = i+1
    print(newList)

even(2,3)
even2(2,3)


# if __name__ == '__main__':
#     even(2,3)
#     even2(2,3)




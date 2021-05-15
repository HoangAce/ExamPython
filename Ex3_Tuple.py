TupleA = tuple()
TupleB = tuple()
def distinct ( tup):
    n=0
    for t in tup:
        for k in tup:
            #print t,k,n
            if (t == k ):
                n = n+1
    if ( n != len(tup)):
        return False
    else :
        return True
def checkElement (tupA, tupB):
    if tupB in tupA:
        return True
    else :
        return False
print("Plese enter TupleA")
TupleA = input()
print("Plese enter TupleB")
TupleB = input()
if distinct (TupleA):
    print("TuplesA contain unique values")
else:
    print("tuplesA don't contain unique values")
if distinct (TupleB):
    print("TuplesB contain unique values")
else:
    print("tuplesB don't contain unique values")
if checkElement(TupleA, TupleB):
    print("tuple A contains all elements of tuple B")
else:
    print("tuple A don't contains all elements of tuple B")

from collections import Counter,defaultdict
from HeapTest import BinHeap


def string2freq(x): # x is a string of symbols from alphabet.
    S = sorted(set(x)) #Can I use this?
    f = list()
    for character in S:
        f.append(x.count(character))
    return S, f

def huffmanEncode(S, f): # f is a vector of symbol frequencies, from above
    #TODO: Heap = minheap() // initialize minHeap from class.
    H = BinHeap() # H.initialize
    for i in range(len(S)):
        #TODO: H.insert(i(f[i]))
        print("")


def encodeString():
    # TODO:
    print("")



#Testhing...

print(string2freq("asd!!!$$###fasdas"))
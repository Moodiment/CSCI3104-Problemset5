from collections import Counter,defaultdict
from HeapTest import MinHeap


def string2freq(x): # x is a string of symbols from alphabet.
    S = sorted(set(x)) #Can I use this?
    f = list()
    for character in S:
        f.append(x.count(character))
    return S, f

def huffmanEncode(S, f): # f is a vector of symbol frequencies, from above
#create huffman tree. Depth first search on huffman encode, add binary code to dictionary with key as key.
    #TODO: Heap = minheap() // initialize minHeap from class.
    H = minHeap() # H.initialize
    n = len(f)
    for i in range(len(n)):
        H.insert(f[i],S[i]) #Insert frequency, characater
    for k in range(len(f)):
        i = H.delMin()
        j = H.delMin()


def encodeString():
    # TODO:
    print("Placeholder print")



#Testhing...

print(string2freq("asd!!!$$###fasdas"))

epid={
    111:45, 
    121:89,
    131:76,
    141:94    }

epid2={
    222:56,333:87,444:56
}

epid.update(epid2)
print(epid)

#to  creat empty dictinary or to remove all items in dic. 
#epid.clear()

empt={} #empty dict.
epid.popitem()  # used to remove last item in the list
epid.pop(121)   # used to remove specific item from the list
print(epid)
# or del epid[121]

# to delete dict 
# del epid
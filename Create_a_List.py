list = [10,20,30]

list.append(40)       # Adds 40 at the end of the list                     10,20,30,40
list.count(20)        # Counts occurrences of 20 in the list               1
list.extend([50,60])  # Extends list by adding elements from another list  10,20,30,40,50,60
list.insert(2,25)     # Inserts 25 at index 2                              10,20,25,30,40,50,60
list.remove(30)       # Removes first occurrence of 30 from the list       10,20,25,40,50,60
list.pop()            # Removes and returns the last item in the list      60
list.sort()           # Sorts the list in ascending order                  10,20,25,40,50
list.reverse()        # Reverses the order of the list                     50,40,25,20,10

print(list)
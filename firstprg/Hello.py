list1 = [12, 23, 34, 45, 23, 67, 27]
print("0. create a list: ", list1)
OP1 = list1.append(16)      # appending a number 12 to the list
print("1. operation append: ", list1)
list1.remove(34)
print("2. operation remove: ", list1)
list1.reverse()
print("3. operation reverse: ", list1)
list1.sort()
print("4. operation sort: ", list1)
list1.copy()
print("5. operation copy: ", list1)
list2 = [4, 45]
print("   list2: ", list2)
list1.extend(list2)
print("6. operation extend: ", list1)
print(list1)
# for i in range(len(list1)):
   # count1 = list1.count(list1[i])
   # j = str(list1[i])
   # if int(count1) > 1:
        # print("7. operation count of repeated member " + j + ":" + str(count1))
      #  list1.remove(list1[i])
      #  print(list1[i])
  #  else:
       # pass






















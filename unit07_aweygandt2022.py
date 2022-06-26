############################################################
#     Aidan Weygandt                        05.13.21       #
#     Unit 7 Problems                                      #
#     Count Digits, Smallest index of list, List shuffle   #
#     Revise selection sort, bubble sort, merge sort       #
#     Locker Problem                                       #
############################################################


import random
numbers1 = []
for num in range(0, 1000): numbers1.append(random.randint(0, 9)) #makess list of 1000 numbers from 0-9
count1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for each in numbers1: count1[each] += 1 #counts total of each number
print("Problem #1 - Count of Digits")
for each in range(0, 10): #prints each number and it's count
  print("There are", count1[each], each, end="")
  print("'s", "in the list")


def indexOfSmallestElement(list): #returns minimum value's index in a list
  minindex = list.index(min(list))
  return minindex

numbers2 = []
for num in range(0, 15): numbers2.append(random.randint(0, 100)) #makes list of 15 random numbers from 0-100
print("\n\nProblem #2 - Smallest Index")
print("The smallest number is", numbers2[indexOfSmallestElement(numbers2)], "at the index", indexOfSmallestElement(numbers2))
print("The full list is:")
print(numbers2)


def shuffle(list): #randomly shuffles items in a list
  shuffledList = []
  randlist = []
  rand = random.randint(0, 9)
  while len(randlist) < 10:
    while rand in randlist: #if numbers already in list find a number thats not
      rand = random.randint(0, 9)
    randlist.append(rand) #add the number to the list
  for num in randlist:
    shuffledList.append(list[num]) #adds item from input list to shuffled list at random index
  return shuffledList

print("\n\nProblem #3 - List Shuffle")
numbers3 = []
for num in range(0, 10): numbers3.append(random.randint(0, 100)) #makes list of 10 random numbers from 0-100
print("List:")
print(numbers3)
numbers3.sort()
print("Sorted List:")
print(numbers3)
print("Shuffled List:")
print(shuffle(numbers3)) #shuffles list


#sorts list
#starts at beginning of list
#finds smallest number in list and swaps with first item
#next smallest is swapped with next index in list
def selectionSortsm(lst):
  swaps = 0  #swaps counts how many times numbers were swapped to get the list in order
  for i in range(len(lst)):
    # Find the minimum in the lst[i : len(lst)]
    currentMin = lst[i]
    currentMinIndex = i
    
    for j in range(i + 1, len(lst)):
      if currentMin > lst[j]:
        currentMin = lst[j]
        currentMinIndex = j
    
    # Swap lst[i] with lst[currentMinIndex] if necessary
    if currentMinIndex != i:
      lst[currentMinIndex] = lst[i]
      lst[i] = currentMin
      swaps += 1
  print(lst)
  print("Swaps:", swaps)

def selectionSortlg(lst): #finds largest item and swaps with last index, then second largest and swaps with second to last index and so on
  swaps = 0
  for i in reversed(range(len(lst))):
    currentMax = lst[i]
    currentMaxIndex = i
    
    for j in reversed(range(0, i)):
      if currentMax < lst[j]:
        currentMax = lst[j]
        currentMaxIndex = j
    
    if currentMaxIndex != i:
      lst[currentMaxIndex] = lst[i]
      lst[i] = currentMax
      swaps += 1
  print(lst)
  print("Swaps:", swaps)

print("\n\nProblem #4 - Revise Selection Sort")
numbers4L1 = []
for num in range(0, 10): numbers4L1.append(random.randint(0, 9)) #makes list of 10 random numbers from 0-9
numbers4L2 = numbers4L1.copy()
print("Unsorted list:")
print(numbers4L1)
print("List sorted with selectionSortsm:")
selectionSortsm(numbers4L1)
print("Unsorted copy of list:")
print(numbers4L2)
print("Copy of list sorted with selectionSortlg:")
selectionSortlg(numbers4L2)


def bubbleSwap(list): #swaps item with item after if smaller unil the list is in order
  swap = 0
  end = 1
  while list: 
    end = 0
    for num1 in range(0, 10):
      if num1 != 9:
        if list[num1] > list[num1+1]:
          list[num1], list[num1+1] = list[num1+1], list[num1]
          swap += 1
          end = 1
    if end == 0: break
  print(list)
  print("Swaps:", swap)

print("\n\nProblem #5 - Bubble Sort")
numbers5 = []
for num in range(0, 10): #makes list of 10 random numbers from 0-9
  numbers5.append(random.randint(0, 9))
print("Unsorted list:")
print(numbers5)
print("List sorted with bubble sort:")
bubbleSwap(numbers5)


def merge(list1, list2):
  mergedList = []
  min1 = 0
  min2 = 0
  swaps = 0
  while len(mergedList) < 10: #take min from each list compares them and then orders them in a new list
    min1, min2 = min(list1), min(list2)
    list1.remove(min1)
    list2.remove(min2)
    if swaps == 4:
      min3, min4 = min(list1), min(list2)
      if min1 < min4 and min2 < min3:
        if min1 < min2:
          mergedList.append(min1)
          mergedList.append(min2)
        else: 
          mergedList.append(min2)
          mergedList.append(min1)
      elif min4 < min1:
        list1.append(min1)
        if min2 < min4:
          mergedList.append(min2)
          mergedList.append(min4)
        else: 
          mergedList.append(min4)
          mergedList.append(min2)
      elif min3 < min2:
        list2.append(min2)
        if min2 < min4:
          mergedList.append(min1)
          mergedList.append(min3)
        else: 
          mergedList.append(min3)
          mergedList.append(min1)
    else:
      if min1 < min2:
          mergedList.append(min1)
          mergedList.append(min2)
      else:
          mergedList.append(min2)
          mergedList.append(min1)
    swaps += 1
  print(mergedList)
  print("Swaps:", swaps)
  return mergedList

print("\n\nProblem #6 - Merge Sort")
numbers6L1 = []
numbers6L2 = []
for num in range(0, 5): #makes two lists of 5 random numbers from 0-9
  numbers6L1.append(random.randint(0, 9))
  numbers6L2.append(random.randint(0, 9))
print("Two unsorted lists:")
print(numbers6L1, numbers6L2)
print("Two lists sorted with merge sort:")
merge(numbers6L1, numbers6L2)


def Students(list): #takes 100 boolian varibles switches them all. then every other variable. then every third and continues until every one hundredth.
  for student in range(0, 100):
    for locker in range(student, 100, student+1):
      list[locker] = not(list[locker])
  return list

print("\n\nProblem #7 - Locker Problem")
lockerList = 100*[False]
locker = 0
Students(lockerList)
for each in lockerList: #prints every locker thats open/every true boolian variable in lockerlist
  if each:
    print("Locker", locker+1, "is open")
  locker += 1
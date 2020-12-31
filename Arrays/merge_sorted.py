
def merge_sorted(l1, l2):

  result = []

  while(len(l1) > 0 and len(l2) > 0):
  
    if (l1[0] <= l2[0]):

      result.append(l1[0])
      l1.remove(l1[0]) 

    else:

      result.append(l2[0])
      l2.remove(l2[0])

  if len(l1) > 0:
    result += l1[0:]
  
  elif len(l2) > 0:
    result += l2[0:]

  return result

print(merge_sorted([1,1,6,30,200,300], [0,3,4,5,31]))


def cycleSort(array):
writes = 0

for cycleStart in range(0, len(array) - 1):
	item = array[cycleStart]
	
	pos = cycleStart
	for i in range(cycleStart + 1, len(array)):
	if array[i] < item:
		pos += 1
	
	if pos == cycleStart:
	continue
	
	while item == array[pos]:
	pos += 1
	array[pos], item = item, array[pos]
	writes += 1
	
	while pos != cycleStart:
	
	pos = cycleStart
	for i in range(cycleStart + 1, len(array)):
		if array[i] < item:
		pos += 1
	
	while item == array[pos]:
		pos += 1
	array[pos], item = item, array[pos]
	writes += 1

return writes
arr = [1, 8, 3, 9, 10, 10, 2, 4 ]
n = len(arr)
cycleSort(arr)

print("After sort : ")
for i in range(0, n) :
	print(arr[i], end = \' \')

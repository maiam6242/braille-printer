import numpy as np

array1 = np.array([[1,2],[3,4],[5,6]])
array2 = np.array([[7,8],[9,10],[11,12]])
line1 = []
line2 = []
lines = []

line1.append(array1)
line1.append(array1)
line1.append(array1)
line1.append(array1)
line1.append(array1)

line2.append(array2)
line2.append(array2)
line2.append(array2)
line2.append(array2)
line2.append(array2)

lines.append([np.asarray(line1)])
lines.append([np.asarray(line2)])

stacked = np.vstack((np.asarray(lines)))
row = stacked[0]
print(stacked)
print(np.shape(stacked))
print('0: num rows')
print(np.shape(row))
start_num = 0
for pod_row in range(3):
    for pod_col in range(2):
        for pod_num in range(start_num,np.shape(row)[0],2):
            print('Pod Num %s' %pod_num)
            print('Pod Col %s' %pod_col)
            print('Pod Row %s' %pod_row)
            print('Val %s' %row[pod_num, pod_row, pod_col])
            print('Start Num %s' %start_num)
            # line_one.append(row1[pod_num,pod_row,pod_col])
    start_num += 1    
# print(np.shape(stacked[0,:]))
# print(stacked[:,:,0])
# print(stacked[0,4,0,0])
# print(stacked[0,:])
# for i in range(0,4):
#     print(stacked[0,i,0])
# print(stacked[0,0,0])
# print(stacked[0,:,0])
# print(stacked[0])
print('1: num columns')
print(np.shape(stacked[:,1]))
print(np.shape(stacked[:,2]))
print(np.shape(stacked[:,3]))

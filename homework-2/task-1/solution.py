

        
# with open('input.txt') as f:
#     content = f.read().split('\n')
#     # print(content)
#     is_tree = True
#     (peaks, *data_peaks) = content

#     print('data peaks', data_peaks)
   
#     max_left = 0
#     max_right = 0


    
peaks = int(input())
tree = []
for _ in range(peaks):
  v, l, r = input().split()
  tree.append([int(v), int(l), int(r)])
# print(tree)
flag = True
root = 0

stack_list = [(root, float("-inf"), float("inf"))]
while stack_list and flag:
    i, low, high = stack_list.pop()
    val, left, right = tree[i]

    if not (low < val < high):
        flag = False
        break

    if right != -1:
        stack_list.append((right, val, high))
    if left != -1:
        stack_list.append((left, low, val))

result = str(flag).upper()
print(result)

    


# print(result if result != max_limit else -1)

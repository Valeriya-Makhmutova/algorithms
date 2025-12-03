with open('input.txt', encoding='utf-8') as f:
    data = f.read().strip().split('\n')
    max_weight = int(data[0])
    items = int(data[1])
    
    if items == 0:
        items_weight = []
    else:
        items_weight = list(map(int, data[2].split()))
    
    dp = [False] * (max_weight + 1)
    dp[0] = True

    for w in items_weight:
        for j in range(max_weight, w - 1, -1):
            if dp[j - w]:
                dp[j] = True
    
    result = 0
    for j in range(max_weight, -1, -1):
        if dp[j]:
            result = j
            break
    
    with open('output.txt', 'w', encoding='utf-8') as file:
        file.write(str(result))

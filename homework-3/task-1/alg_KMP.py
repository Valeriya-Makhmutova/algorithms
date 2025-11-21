import re
def build_prefix_function(pattern):
   
    m = len(pattern)
    pi = [0] * m  
    k = 0 
    
    for i in range(1, m):
        while k > 0 and pattern[k] != pattern[i]:
            k = pi[k - 1]
        
        if pattern[k] == pattern[i]:
            k += 1
        
        pi[i] = k
    
    return pi

def levenshtein_distance(str1, str2):

    m, n = len(str1), len(str2)
    
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i  
    
    for j in range(n + 1):
        dp[0][j] = j  

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                cost = 0  # символы одинаковые
            else:
                cost = 1  # символы разные, нужна замена
            
            dp[i][j] = min(
                dp[i - 1][j] + 1,      # удаление
                dp[i][j - 1] + 1,      # вставка
                dp[i - 1][j - 1] + cost  # замена или совпадение
            )
    
    return dp[m][n]


with open('input.txt', encoding='utf-8') as f:
    data = f.read().split('\n')
    # text = data[0]
    text = re.sub(r'[^a-zA-Zа-яА-ЯёЁ!?]|\s+', ' ', data[0])
    # print(re.sub(r'[^a-zA-Zа-яА-ЯёЁ!\.?]|\s+', ' ', data[0]))
    k_ind = int(data[1])

    list_words_data = []
    max_pref_sum = 0
    resume = ''
    words = text.lower().split()
 
# 1 часть:

    for ind, word in enumerate(words):
        word_pref_sum = sum(build_prefix_function(word))

        if word_pref_sum > max_pref_sum:
            max_pref_sum = word_pref_sum
        
        list_words_data.append({'word_pref_sum': word_pref_sum, 'word': word, 'length': len(word), 'index': ind})

    list_win_words1 = []
    for word_dict in list_words_data:
        if word_dict['word_pref_sum'] == max_pref_sum:
            list_win_words1.append(word_dict)


    list_win_words2 = []
    max_length = 0
  
    if len(list_win_words1) > 1:
        for elem in list_win_words1:
            # print("elem['length']", elem['length'])
            if elem['length'] > max_length:
                # print(max_length)
                max_length = elem['length']
        
        for elem2 in list_win_words1:
            if elem2['length'] == max_length:
                list_win_words2.append(elem2)
  
        resume = list_win_words2[0]
    else:
        resume = list_win_words1[0]
    
# 2 часть:
    total_words = 0
    gen_word = resume['word']
 
    for word in words:
        if (levenshtein_distance(gen_word, word) <= k_ind) and (gen_word != word):
            total_words += 1

    file = open('output.txt', 'w', encoding='utf-8')
    result = [gen_word, str(resume['word_pref_sum']), str(total_words)]
    file.write('\n'.join(result)) 

    
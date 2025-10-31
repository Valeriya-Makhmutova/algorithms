with open('input.txt', encoding='utf-8') as f:
  words = sorted(f.readline().split())
  dict_of_words = {}

  for word in words:
    sorted_word = sorted(list(word.lower()))
    joined_word = "".join(sorted_word)

    if joined_word not in dict_of_words:
      dict_of_words[joined_word] = []

    dict_of_words[joined_word].append(word)

  file = open('output.txt', 'w')
  strings_list = []
  for coll_of_lett in dict_of_words:
    string = " ".join(dict_of_words[coll_of_lett])
    strings_list.append(string)
    
  if strings_list:
    file.write('\n'.join(strings_list)) 

def main():
    with open('input.txt', 'r', encoding='utf-8') as f:
        data = f.read().splitlines()
    
    n = int(data[0].strip())
    codes = {}
    for i in range(1, 1 + n):
        line = data[i].strip()
        parts = line.split(',')
        if len(parts) < 2:
            continue
        char = parts[0].strip()[1:]
        code = parts[1].strip()[:-1]
        codes[code] = char

    bit_string = data[1 + n].strip()

    decoded_string = ""
    current_bits = ""
    for bit in bit_string:
        current_bits += bit
        if current_bits in codes:
            decoded_string += codes[current_bits]
            current_bits = ""
    
    def backtrack(i, used):
        if i == len(decoded_string):
            return 0
        max_count = 0
        for j in range(i + 1, len(decoded_string) + 1):
            substr = decoded_string[i:j]
            if substr not in used:
                used.add(substr)
                count = 1 + backtrack(j, used)
                if count > max_count:
                    max_count = count
                used.remove(substr)
        return max_count

    def greedy(s):
        used = set()
        i = 0
        count = 0
        while i < len(s):
            found = False
            for j in range(i + 1, len(s) + 1):
                substr = s[i:j]
                if substr not in used:
                    used.add(substr)
                    count += 1
                    i = j
                    found = True
                    break
            if not found:
                substr = s[i:]
                if substr and substr not in used:
                    used.add(substr)
                    count += 1
                i = len(s)
        return count

    if len(decoded_string) <= 20:
        result = backtrack(0, set())
    else:
        result = greedy(decoded_string)
    
    with open('output.txt', 'w', encoding='utf-8') as f:
        f.write(str(result))



if __name__ == "__main__":
    main()


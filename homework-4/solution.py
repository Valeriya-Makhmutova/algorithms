with open('input.txt', encoding='utf-8') as f:
        lines = f.read().strip().splitlines()
        n = int(lines[0])
        segments = []
        
        for i in range(1, n + 1):
            if i < len(lines):
                s, f = map(int, lines[i].split())
                segments.append((s, f))
        
        segments.sort(key=lambda x: x[1])
        
        points = []
        current_point = -1
        
        for s, f in segments:
           
            if current_point < s or current_point > f:
                current_point = f
                points.append(current_point)
        
        with open('output.txt', 'w', encoding='utf-8') as out:
            out.write(str(len(points)))
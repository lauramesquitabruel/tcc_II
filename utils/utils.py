def contem_bloco(s, n, bloco):
    m = len(bloco)
    
    if m > n:
        return False
        
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if s[i + j] != bloco[j]:
                match = False
                break
        if match:
            return True
            
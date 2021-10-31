def KMPSearch(pat, txt):
    M, N = len(pat), len(txt)
  
    # create pi[] that will hold the longest prefix suffix 
    # values for pattern
    pi = [0]*M
    j = 0 # index for pat[]
  
    # Preprocess the pattern (calculate pi[] array)
    compute_pi(pat, M, pi)
  
    i = 0 # index for txt[]
    matches = []
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
  
        if j == M:
            matches.append(str(i-j))
            j = pi[j-1]
  
        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match pi[0..pi[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = pi[j-1]
            else:
                i += 1
    return matches
  
def compute_pi(pat, M, pi):
    len = 0 # length of the previous longest prefix suffix
    i = 1
  
    # the loop calculates pi[i] for i = 1 to M-1
    while i < M:
        if pat[i]== pat[len]:
            len += 1
            pi[i] = len
            i += 1
        else:
            if len != 0:
                len = pi[len-1]
            else:
                pi[i] = 0
                i += 1

while True:
    try:
        pattern = input()
        text = input()
        print(" ".join(KMPSearch(pattern,text)))

    except EOFError:
        break
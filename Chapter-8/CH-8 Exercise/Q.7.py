def rem(l,word):
    n = []
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n

l = ["satwik","Satyam","man","but","so","am"]
print(rem(l,"am"))
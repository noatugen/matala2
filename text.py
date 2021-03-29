def revword(word):   
    word = word.lower()
    length = len(word)
    wordn=''
    for i in word:
        wordn=wordn+word[length-1]
        length=length-1
    return wordn    

def countword()->int:
    text = open('text.txt')
    i=0
    countera=1
    for line in text:
        line=line.rstrip();
        if i==0:
            word=line
            i=1
            continue
        words=line.split()
        for w in words:
            w_new=revword(w)
            if w_new==word:
                countera=countera+1
    return countera
print(countword())
                
                
        
            
            
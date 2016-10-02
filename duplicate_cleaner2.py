"""After making the original duplicate_cleaner I was at
www.pythonlearn.com/html-008/cfbook017.html and read the exercise which
suggested doing multiple erasure by first constructing a dictionary based
file size. Curious to see if it was tidier I wrote the following version of
duplicate_cleaner."""

import os
import filecmp


def remove_duplicates(folder):
    K={}
    T=[]
    count=0
    for root,directory,files in os.walk(folder):
        for file in files:
            filename=os.path.join(root,file)
            t=os.path.getsize(filename)
            if t not in K:
                K[t]=[filename]
            else:
                K[t].append(filename)
    for key in K:
        if len(K[key])>1:
            for filename1 in K[key]:
                for filename2 in K[key]:
                    if filename2 is filename1:
                        continue
                    elif filecmp.cmp(filename1,filename2,False):
                        os.remove(filename2)
                        K[key].remove(filename2)
                        count+=1
                        T.append(filename2)
    print(count,'files deleted')
    print('deleted files are:')
    for item in T:
        print(item)
                    
    
    

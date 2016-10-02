"""a short script written to clean up my very messy iphoto library. It is
generalized to work for any folder with suspected duplicates. Although the
nesting is a little ugly, the program works very simply."""

import os
import filecmp

def check_files(folder):
    print(folder)
    count=0
    for path,directory,files in os.walk(folder):
        for file1 in files:
            filename1=os.path.join(path,file1)
            print('file1 is:',filename1)
            for path,directory,files in os.walk(folder):
                for file2 in files:
                    filename2=os.path.join(path,file2)
                    print('file2 is:',filename2)
                    if filename1!=filename2:
                        if os.path.getsize(filename1)==os.path.getsize(filename2):
                            print('\t{0} and {1}\n\tare the same size!\n'.format
                                  (filename1,filename2))
                            if filecmp.cmp(filename1,filename2,False):
                                print('\t\t',filename1,'\n\t\t'
                                      'and',filename2,'\n\t\tare identical!\n\t\t',
                                      filename2,'deleted.')
                                os.remove(filename2)
                                count+=1
                                check_files(folder)
                    else:
                        continue
    print('folder checked and {0} duplicates removed'.format(count))
    
if __name__=='__main__':

    folder=input('Check which folder for duplicates?')
    check_files(folder)

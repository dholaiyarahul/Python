fileObject= open('temp.txt','w+')
print('File Content:')
print(fileObject.read())

fileObject.write('\nPython is simple ane fun to learn.')
print('FIle after adding:')
fileObject.seek(0)
print(fileObject.read())

fileObject.close()
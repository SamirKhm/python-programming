# append to an existing file
# It should add data about John Foe's Hometown

f=open("samir.txt","a")
string='''
John doe initially lived in Phoenix , Arizona.
He is a very nice guy'''

f.write(string)
f.close()
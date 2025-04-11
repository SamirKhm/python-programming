#OS
import shutil
import os
a=os.listdir("dir")

print(a)
print(os.getcwd())
print(os.path.exists("dir"))
# os.remove("samplefile1.txt")
# os.rmdir("dir")

# shutil.rmtree("dir")

shutil.copy("samir.txt","samplefile1.txt")

shutil.move("samplefile1.txt","Desktop")
# Write to a file called John Doe.txt
# It should contain data about John Doe

f=open("x.txt","w")
string='''
Samir is a nice guy
He lives in NYC
and his favourite package in Pandas'''
f.write(string)
f.close()
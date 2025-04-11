try:
    a=345/0

except Exception as e:
    print(e)

else: # gets executed when there is no error
    print("Hey I am good")
    
finally:
    print("Run if error occurs or not")
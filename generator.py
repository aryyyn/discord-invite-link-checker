import random
import string
import os




try:
    python_file = open('discordinvitelinks.txt', "w")
    length = 5
    while(length!=0):
        res = ''.join(random.choices(string.ascii_letters + string.digits, k= 8))
        print(res)
        python_file.write(res + '\n')

except Exception as err:
    print(err)
    
   



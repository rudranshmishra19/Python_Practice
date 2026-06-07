def question(prompt,retries=4,reminder='pls try again'):
    while True:
        reply=input(prompt)
        if reply in {'y','yo','yes'}:
            return True
        if reply in {'n','no','nope'}:
            return False
        retries-=1
        if retries<=0:
            raise ValueError('retires ended ')
        print(reminder)

question('how muh can you see')
name=input('What is your name?')
print('Nice to meet you',name)

def hru(lang):
    if lang=='spanish':
        return'como estas?'
    elif lang=='french':
        return'comment ca va?'
    else:
        return'how are you doing?'
    
print(hru('english'),name)
print(hru('spanish'),name)
print(hru('french'),name)
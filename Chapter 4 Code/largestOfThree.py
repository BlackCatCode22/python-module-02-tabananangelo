a=input('How many points did player a score in their career?')
b=input('How many points did player b score in their career?')
c=input('How many points did player c score in their career?')

if a>b:
    if a>c:
        print('Player a is the best scorer, scoring',a)
    else:
        print('Player c is the best scorer, scoring',c)
else:
    if b>c:
        print('Player b is the best scorer, scoring',b)
    else:
        print('Player c is the best scorer, scoring',c)
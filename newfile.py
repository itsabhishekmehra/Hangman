def words(eklist):
    a= 'abcdefghijklmnopqrstuvwxyz'
    for i in eklist:
        a=a.replace(i,'')
    print(a)
b=["a","b"]
words(b)
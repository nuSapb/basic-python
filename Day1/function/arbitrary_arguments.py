def some_method(*a, **kw):
    for arg in a:
        print(arg)
    for key, value in kw.items():
        print('%s: %s' % (key, value))

# call function
some_method(1,2,3, name="Anu", phone='0989999999', test='8')
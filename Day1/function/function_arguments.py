# Positional
def add(x, y):
    return x + y

# Keyword
def shout(phrase='Yipee!'):
    print(phrase)

# Positional + Keyword
def echo(text, prefix=''):
    print('%s%s' % (prefix, text))


print(add(1,2))
shout()
shout('Hello')
echo('Anu')
echo('Anu', 'Mr.')
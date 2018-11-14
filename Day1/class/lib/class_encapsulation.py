class Base(object):
    def __init__(self):
        print('__init__ base class')

class User(Base):
    __name = None
    __is_staff = False

    def __init__(self, name='Anonymous'):
        self.__name = name
        super(User, self).__init__()

    @property
    def is_authorized(self):
        return self.__is_staff

    @is_authorized.setter
    def is_authorized(self, value):
        self.__is_staff = value
        
    @property
    def name(self):
        return self.__name
        
    @name.setter
    def name(self, value):
        self.__name = value



'''
anonymous = User()
print(anonymous.name)

print(anonymous.is_authorized)

anonymous.name = 'Anu'
anonymous.is_authorized = True

print(anonymous.name, anonymous.is_authorized)
'''
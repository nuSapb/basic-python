class User(object):
    name = None
    is_staff = False

    def __init__(self, name='Anonymous'):
        self.name = name
        super(User, self).__init__()

    def is_authorized(self):
        return self.is_staff

class SuperUser(User):
    is_staff = True

superUser = SuperUser('Anu Sakpibal')
print(superUser.name)

print(superUser.is_authorized())
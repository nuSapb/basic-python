class User(object):
    name = None
    is_staff = False

    def __init__(self, name='Anonymous'):
        self.name = name
        super(User, self).__init__()

    def is_authorized(self):
        return self.is_staff

anonymous = User()
print(anonymous.name)

print(anonymous.is_authorized())
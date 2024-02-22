class Account:
    def __init__(self, username, email, date_joined):
        self.username = username
        self.email = email
        self.date_joined = date_joined

    def __str__(self):
        return '%s (%s)' % (self.username, self.email)

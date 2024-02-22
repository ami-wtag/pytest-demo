import datetime
import factory

import objects


class AccountFactory(factory.Factory):
    class Meta:
        model = objects.Account

    username = factory.Sequence(lambda n: 'rafsun%s' % n)
    email = factory.LazyAttribute(lambda o: '%s@example.org' % o.username)
    date_joined = factory.LazyFunction(datetime.datetime.now)


mock_account = AccountFactory()
print(mock_account)

mock_accounts = AccountFactory.build_batch(5)
for account in mock_accounts:
    print(account)

"""
Example
-------
rafsun0 (rafsun0@example.org)
rafsun1 (rafsun1@example.org)
rafsun2 (rafsun2@example.org)
rafsun3 (rafsun3@example.org)
rafsun4 (rafsun4@example.org)
rafsun5 (rafsun5@example.org)
"""

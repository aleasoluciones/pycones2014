
from expects import expect, be_true, raise_error

with description('Register user'):

    with before.each:
        self.nickname = '@foolano'

    with it('registers a new user'):
        # Register a user
        # Validate that the user is registered
        pass

    with context('when user already exists'):
        with it('raises error'):
            # Register a user
            #
            pass

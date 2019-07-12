class UsersRouter(object):

    models = ['kiwi_users', 'kiwi_lino', 'kiwi_lin', 'kiwi_vid', 'kiwi_child', 'kiwi_game']

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.models:
            return 'kiwi'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write events models go to eventsDB.
        """
        if model._meta.app_label in self.models:
            return 'kiwi'
        return None

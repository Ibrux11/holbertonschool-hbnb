class DataManager:
    def __init__(self, use_database=False):
        self.use_database = use_database

    def save_user(self, user):
        if self.use_database:
            db.session.add(user)
            db.session.commit()
        else:
            self.save_user_to_file(user)

    def save_user_to_file(self, user):
        pass

    def get_user(self, user_id):
        if self.use_database:
            return User.query.get(user_id)
        else:
            return self.get_user_from_file(user_id)

    def get_user_from_file(self, user_id):
        pass

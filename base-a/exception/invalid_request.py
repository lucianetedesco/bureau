class InvalidRequest(Exception):

    def to_dict(self):
        rv = dict()
        rv['message'] = self.args[0]
        self.status_code = self.args[1] if len(self.args) > 1 else 400
        return rv

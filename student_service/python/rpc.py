from nameko.rpc import rpc
from db.dbconfig import db, Students


class Service:
    name = "student"

    @rpc
    def insert(self, firstname, lastname, email):
        new_log = Students(
            firstname = firstname,
            lastname = lastname,
            email = email
        )
        db.add(new_log)
        db.commit()

        return new_log.id




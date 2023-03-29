from db.dbconfig import db, Enroll
from nameko.rpc import rpc

class Service:
    name = 'enroll'

    @rpc
    def insert(self, id, firstname, lastname):
        subjects_id = ['081102', '520101', '511100', '517121']
        for subject in subjects_id:
            newlog = Enroll(
                id = id,
                name = f'{firstname} {lastname}',
                subjectid = subject,
                term = 1,
                year = 2566
            )
            db.add(newlog)
            db.commit()
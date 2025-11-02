from sqlalchemy import create_engine, text
from sqlalchemy import sessionmaker

class SubjectTable:
   
    __scripts = {
        "select_all": text("SELECT * FROM subject"),
        "select by id": text("SELECT * FROM subject WHERE subject_id = :id"),
        "insert": text("INSERT INTO subject (subject_title) VALUES (:title) RETURNING subject_id"),
        "update": text("UPDATE subject SET subject_title = :new_title WHERE subject_id = :id"),
        "delete": text("DELETE FROM subject WHERE subject_id = : id")
    }
    
    def __init__(self, connection_string):
        self.db = create_engine(connection_string)
        
    def get_all_subjects(self):
        with self.db.connect() as session:
            result = session.execute(self.__scripts["select_all"])
            return result.mappings().all()
            
    def get_subject_by_id(self, id):
        with self.db.connect() as session:
            result = session.execute(self.__scripts["select_by_id"], {"id": id})
            return result.mappings().first()
    
    def add_subject(self, title):
        with self.db.connect() as session:
            result = session.execute(self.__scripts["insert"], {"title": title})
            session.commit()
            return result.scalar_one()
    
    def update_subject(self, id, new_title):
        with self.db.connect() as session:
            session.execute(self.__scripts["update"], {"id": id, "new title": new_title})
            session.commit()

    def delete_subject(self, id):
        with self.db.connect() as session:
            session.execute(self.__scripts["delete"], {"id": id})
            session.commit()


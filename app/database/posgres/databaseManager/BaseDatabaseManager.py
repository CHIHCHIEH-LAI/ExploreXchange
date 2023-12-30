from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import create_engine

class BaseDatabaseManager:
    def __int__(self, database_uri):
        engine = create_engine(database_uri)
        self.session = sessionmaker(engine)

    def create(self, data):
        session = self.Session()
        try:
            session.add(data)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            session.close()

    # def query(self, model, id):
    #     session = self.Session()
    #     try:
    #         instance = session.query(model).get(id)
    #         return instance
    #     except SQLAlchemyError as e:
    #         raise e
    #     finally:
    #         session.close()

    # def update(self, model, id, update_data):
    #     session = self.Session()
    #     try:
    #         instance = session.query(model).get(id)
    #         if instance:
    #             for key, value in update_data.items():
    #                 setattr(instance, key, value)
    #             session.commit()
    #             return instance
    #         else:
    #             return None
    #     except SQLAlchemyError as e:
    #         session.rollback()
    #         raise e
    #     finally:
    #         session.close()

    # def delete(self, model, id):
    #     session = self.Session()
    #     try:
    #         instance = session.query(model).get(id)
    #         if instance:
    #             session.delete(instance)
    #             session.commit()
    #             return True
    #         else:
    #             return False
    #     except SQLAlchemyError as e:
    #         session.rollback()
    #         raise e
    #     finally:
    #         session.close()
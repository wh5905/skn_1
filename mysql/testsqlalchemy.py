from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base



#데이터베이스 연결 설정
DATABASE_URL = "mysql+mysqlconnector://root:@localhost/test"

#SQLAlchemy 엔진 생성
engine = create_engine(DATABASE_URL, echo=True)

#베이스 클래스 생성
Base = declarative_base()


#테이블 모델 정의
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)


#데이터베이스에 테이블 생성
Base.metadata.create_all(engine)

#세션 구성
Session = sessionmaker(bind=engine)
session = Session()

#CRUD 작업 예제
#Create (생성)
new_user = User(name="John Doe", age=30)
session.add(new_user)
session.commit()

#Read (읽기)
users = session.query(User).all()
for user in users:
    print(f"ID: {user.id}, Name: {user.name}, Age: {user.age}")

#Update (수정)
user_to_update = session.query(User).filter_by(name="John Doe").first()
user_to_update.age = 31
session.commit()

#Delete (삭제)
user_to_delete = session.query(User).filter_by(name="John Doe").first()
session.delete(user_to_delete)
session.commit()

#세션 닫기
session.close()
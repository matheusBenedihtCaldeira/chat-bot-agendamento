from models.users.models import User, table_registry
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

def test_create_user():

    engine = create_engine(
        'sqlite:///:memory:'
    )
    table_registry.metadata.create_all(engine)
    with Session(engine) as db_session:
        user = User(username='matheus.caldeira', password='12345', email='matheus.caldeira@gmail.com')
        db_session.add(user)
        db_session.commit()
        db_session.refresh(user)
        result = db_session.scalar(
            select(User).where(User.email == 'matheus.caldeira@gmail.com')
        )
        print(result)
    assert result.email == "matheus.caldeira@gmail.com"
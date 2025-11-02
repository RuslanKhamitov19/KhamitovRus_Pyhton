import pytest
from subject_table import SubjectTable
from sqlalchemy import text

CONNECTION_STRING = "postgresql://postgres:123@localhost:5432/QA"

@pytest.fixture
def subject_table():
    table = SubjectTable(CONNECTION_STRING)
    yield table
    with table.db.connect() as session:
        session.execute(text("DELETE FROM subject WHERE subject_title LIKE 'Тест%'"))

def test_add_subject(subject_table):
    title = "Тест предмет"
    new_id = subject_table.add_subject(title)
    assert new_id is not None
    subject = subject_table.get_subject_by_id(new_id)
    assert subject["subject_title"] == title

def test_update_subject(subject_table):
    new_id = subject_table.add_subject("Старый предмет")
    subject_table.update_subject(new_id, "Новый заголовок")
    subject = subject_table.get_subject_by_id(new_id)
    assert subject["subject_title"] == "Новый заголовок"

def test_delete_subject(subject_table):
    new_id = subject_table.add_subject("Удаляемый предмет")
    subject_table.delete_subject(new_id)
    assert subject_table.get_subject_by_id(new_id) is None

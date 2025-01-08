from SubjectTable import SubjectTable

db = SubjectTable("postgresql://postgres:123@localhost:5432/QA")


def test_add_subject():
    before = db.max_count()
    subject_title = "SGL"
    db.add(subject_title)
    after = db.max_count()
    assert before < after
    db.delete(after)


def test_edit_subject():
    subject_title = "SGL"
    db.add(subject_title)
    id = db.max_count()
    new_title = "SQL2.0"
    edit = db.edit(new_title, id)
    db.delete(id)
    assert edit == 1


def test_delete_subject():
    before = db.max_count()
    subject_title = "SGL"
    db.add(subject_title)
    id = db.max_count()
    db.delete(id)
    after = db.max_count()
    assert before == after

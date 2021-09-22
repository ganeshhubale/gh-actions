from ghaction import event
from ghaction import task


def test_event():
    assert event() == "GitHub action event"


def test_task():
    assert task() == "GitHub action task"

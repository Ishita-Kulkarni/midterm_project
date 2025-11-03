from app.history import History

def test_history_clear_alias():
    h = History()
    h.add_entry("x", 1)
    h.clear_history()
    assert h.get_entries() == []

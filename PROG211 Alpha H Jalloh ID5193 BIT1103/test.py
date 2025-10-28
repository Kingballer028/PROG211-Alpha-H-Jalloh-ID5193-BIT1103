# ============================
# test.py
# ============================
from operation import *

def run_tests():
    print("\n--- Running Tests ---")

    print(add_book("111", "Python Basics", "Guido", "Non-Fiction", 4))
    assert "111" in books

    print(add_member(2, "Alice", "alice@mail.com"))
    assert any(m["member_id"] == 2 for m in members)

    print(borrow_book(2, "111"))
    assert books["111"]["available_copies"] == 3

    print(return_book(2, "111"))
    assert books["111"]["available_copies"] == 4

    print(update_book("111", title="Python Advanced"))
    assert books["111"]["title"] == "Python Advanced"

    print(delete_book("111"))
    assert "111" not in books

    print("\n✅ All tests passed successfully!")

if __name__ == "__main__":
    run_tests()

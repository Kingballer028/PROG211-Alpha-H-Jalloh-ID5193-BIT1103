# ============================
# operation.py
# ============================
genres = ("Fiction", "Non-Fiction", "Sci-Fi", "Mystery", "Romance")

books = {
    "9780143127741": {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Fiction",
        "total_copies": 5,
        "available_copies": 5
    }
}

members = [
    {
        "member_id": 1,
        "name": "John Doe",
        "email": "john@example.com",
        "borrowed_books": []
    }
]

def add_book(isbn, title, author, genre, total_copies):
    if isbn in books:
        return "Book already exists!"
    if genre not in genres:
        return "Invalid genre."
    books[isbn] = {
        "title": title,
        "author": author,
        "genre": genre,
        "total_copies": total_copies,
        "available_copies": total_copies
    }
    return f"Book '{title}' added successfully."

def add_member(member_id, name, email):
    for m in members:
        if m["member_id"] == member_id:
            return "Member ID already exists!"
    members.append({
        "member_id": member_id,
        "name": name,
        "email": email,
        "borrowed_books": []
    })
    return f"Member '{name}' added successfully."

def search_book(keyword):
    found = [b for b in books.values() if keyword.lower() in b["title"].lower() or keyword.lower() in b["author"].lower()]
    return found if found else "No book found."

def update_book(isbn, title=None, author=None, genre=None, total_copies=None):
    if isbn not in books:
        return "Book not found!"
    if title: books[isbn]["title"] = title
    if author: books[isbn]["author"] = author
    if genre and genre in genres: books[isbn]["genre"] = genre
    if total_copies:
        books[isbn]["total_copies"] = total_copies
        books[isbn]["available_copies"] = total_copies
    return "Book updated successfully."

def delete_book(isbn):
    if isbn in books:
        del books[isbn]
        return "Book deleted successfully."
    else:
        return "Book not found."

def borrow_book(member_id, isbn):
    member = next((m for m in members if m["member_id"] == member_id), None)
    if not member:
        return "Member not found!"
    if len(member["borrowed_books"]) >= 3:
        return "Borrow limit reached (3 books)."
    if isbn not in books or books[isbn]["available_copies"] == 0:
        return "Book not available."
    books[isbn]["available_copies"] -= 1
    member["borrowed_books"].append(isbn)
    return "Book borrowed successfully."

def return_book(member_id, isbn):
    member = next((m for m in members if m["member_id"] == member_id), None)
    if not member or isbn not in member["borrowed_books"]:
        return "Invalid return."
    member["borrowed_books"].remove(isbn)
    books[isbn]["available_copies"] += 1
    return "Book returned successfully."

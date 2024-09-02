"""
create a library management system. The system will manage different types
of items such as books and magazines and handle operations like borrowing and returning items.

"""
# ------------------------------------
# ------------- functions ------------
# ------------------------------------
# Define data structures
items = {
    "B001": {"type": "book", "title": "1984", "author": "George Orwell", "is_available": True},
    "M001": {"type": "magazine", "title": "National Geographic", "issue_number": "August 2024", "is_available": True}
}

def add_item(item_id, item_type, title, additional_info):
    if item_id not in items:
        items[item_id] = {"type": item_type, "title": title, "is_available": True}
        items[item_id].update(additional_info)
        print(f"{title} added to the library.")
    else:
        print("Item already exists.")

def find_item(item_id):
    return items.get(item_id, None)

def borrow_item(item_id):
    item = find_item(item_id)
    if item:
        if item["is_available"]:
            item["is_available"] = False
            print(f"{item['title']} has been borrowed.")
        else:
            print(f"{item['title']} is currently not available.")
    else:
        print("Item not found.")

def return_item(item_id):
    item = find_item(item_id)
    if item:
        if not item["is_available"]:
            item["is_available"] = True
            print(f"{item['title']} has been returned.")
        else:
            print(f"{item['title']} was not borrowed.")
    else:
        print("Item not found.")

# Example usage
add_item("B001", "book", "1984", {"author": "George Orwell"})
add_item("M001", "magazine", "National Geographic", {"issue_number": "August 2024"})

borrow_item("B001")
return_item("B001")
borrow_item("M001")
return_item("M001")


# ------------------------------------
# -------------- OOP -----------------
# ------------------------------------
class LibraryItem:
    def __init__(self, item_id, title):
        self.item_id = item_id
        self.title = title
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"{self.title} has been borrowed.")
        else:
            print(f"{self.title} is currently not available.")

    def return_item(self):
        if not self.is_available:
            self.is_available = True
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} was not borrowed.")

    def __str__(self):
        return f"{self.title} (ID: {self.item_id})"


class Book(LibraryItem):
    def __init__(self, item_id, title, author):
        super().__init__(item_id, title)
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author} (ID: {self.item_id})"


class Magazine(LibraryItem):
    def __init__(self, item_id, title, issue_number):
        super().__init__(item_id, title)
        self.issue_number = issue_number

    def __str__(self):
        return f"Magazine: {self.title} (Issue: {self.issue_number}, ID: {self.item_id})"


class Library:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.item_id] = item
        print(f"{item} added to the library.")

    def find_item(self, item_id):
        return self.items.get(item_id, None)

    def borrow_item(self, item_id):
        item = self.find_item(item_id)
        if item:
            item.borrow()
        else:
            print("Item not found.")

    def return_item(self, item_id):
        item = self.find_item(item_id)
        if item:
            item.return_item()
        else:
            print("Item not found.")

# Example usage
library = Library()

book1 = Book("B001", "1984", "George Orwell")
magazine1 = Magazine("M001", "National Geographic", "August 2024")

library.add_item(book1)
library.add_item(magazine1)

library.borrow_item("B001")
library.return_item("B001")
library.borrow_item("M001")
library.return_item("M001")

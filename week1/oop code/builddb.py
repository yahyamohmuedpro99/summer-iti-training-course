
import json
#A class to represent a table in the database, including methods for inserting and querying data.


class Table:
    def __init__(self, name):
        self.name = name
        self.rows = []
        self.columns = []
        
    def set_columns(self, columns):
        self.columns = columns

    def insert(self, values):
        if len(values) != len(self.columns):
            raise ValueError("The number of values does not match the number of columns")
        self.rows.append(dict(zip(self.columns, values)))

    def select(self, *columns):
        result = []
        for row in self.rows:
            result_row = {col: row.get(col, None) for col in columns}
            result.append(result_row)
        return result

    def to_dict(self):
        return {
            "columns": self.columns,
            "rows": self.rows
        }

    @classmethod
    def from_dict(cls, data):
        table = cls(name="unknown")
        table.columns = data["columns"]
        table.rows = data["rows"]
        return table
# database clas
## A class to manage multiple tables and handle file storage.

class SimpleDB:
    def __init__(self, filename):
        self.filename = filename
        self.tables = {}
        self.load()

    def create_table(self, name, columns):
        if name in self.tables:
            raise ValueError(f"Table {name} already exists")
        table = Table(name)
        table.set_columns(columns)
        self.tables[name] = table

    def insert_into(self, table_name, values):
        table = self.tables.get(table_name)
        if not table:
            raise ValueError(f"Table {table_name} does not exist")
        table.insert(values)

    def select_from(self, table_name, *columns):
        table = self.tables.get(table_name)
        if not table:
            raise ValueError(f"Table {table_name} does not exist")
        return table.select(*columns)

    def save(self):
        with open(self.filename, 'w') as f:
            json.dump({name: table.to_dict() for name, table in self.tables.items()}, f, indent=4)

    def load(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                for name, table_data in data.items():
                    table = Table.from_dict(table_data)
                    self.tables[name] = table
        except FileNotFoundError:
            pass
# usage
def main():
    db = SimpleDB('db.json')

    # Create a table
    db.create_table('employees', ['id', 'name', 'position'])

    # Insert data into the table
    db.insert_into('employees', [1, 'Alice', 'Engineer'])
    db.insert_into('employees', [2, 'Bob', 'Manager'])

    # Query data from the table
    results = db.select_from('employees', 'name', 'position')
    for row in results:
        print(row)

    # Save the database to a file
    db.save()

if __name__ == "__main__":
    main()

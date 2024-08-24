class Todo:
    def __init__(self, title, description):
        self.title = title
        self.description = description

class TodoApp:
    def __init__(self):
        self.todos = []

    def create(self, title, description):
        pass

    def read(self):
        pass

    def update(self, index, title, description):
        pass

    def delete(self, index):
        pass


# example usage 
# app = TodoApp()
# app.create("Buy groceries", "Milk, Bread, Cheese")
# app.create("Learn Python", "Complete OOP exercises")
# app.read()
# app.update(1, "Learn Advanced Python", "Complete OOP and Data Structures")
# app.read()
# app.delete(0)
# app.read()



##############################################################
# remmber to uncomment this and comment the usage upper #
##############################################################

#app=TodoApp()
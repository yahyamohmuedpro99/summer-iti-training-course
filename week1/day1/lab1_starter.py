class Image:
    def __init__(self, url, alt):
        self.url = url
        self.alt = alt


class task:
    def __init__(self, title, description, image):
        self.title = title
        self.description = description
        self.image = image


class taskApp:
    def __init__(self):
        self.tasks = []

    def create(self, title, description):
        pass

    def read(self):
        pass

    def update(self, index, title, description):
        pass

    def delete(self, index):
        pass


# example usage
# app = taskApp()
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

# app=taskApp()

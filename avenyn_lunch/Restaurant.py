class Restaurant(object):

    def __init__(self, name):
        self.name = name
        self.weekly_menu = [
            [],
            [],
            [],
            [],
            []
        ]

    def add_menu_item(self, dayname, food):
        self.weekly_menu[dayname].append(food)

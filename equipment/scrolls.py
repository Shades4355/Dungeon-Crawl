class Scroll(object):
    def __init__(self, name):
        self.name = name


class Escape(Scroll):
    """A scroll to temporarily escape combat"""
    def __init__(self, name = "scroll: escape"):
        self.name = name

    def escape(self):
        combat = False

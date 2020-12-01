class Scroll(object):
    def __init__(self, name):
        self.name = name


class Escape(Scroll):
    """A scroll to temporarily escape combat"""
    def __init__(self, name = "scroll of escape"):
        self.name = name

    def escape(self, player:object):
        player.inCombat = False
        print("\nEscaping...")

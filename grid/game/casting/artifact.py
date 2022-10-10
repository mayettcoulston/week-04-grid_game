from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!
class Artifact(Actor):
    """An artifact is an actor representing a random objects a gem and a stone. 
    The responsibility of the artifact is to display messages when the robot is passing through it
    """
    def __init__(self):
        super().__init__()
        self._points = 0

    def get_points(self):
        if (self.get_text() == "*"):
            self._points = 1
        else:
            self._points = -1

        return self._points

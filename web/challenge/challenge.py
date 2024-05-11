class Challenge:
    """ Challenge class stores different kinds of challenges, but the pattern is the same. """

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def get_challenge(self) -> ():
        return (self.question, self.answer)
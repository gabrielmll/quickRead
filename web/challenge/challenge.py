class Challenge:
    """ Challenge class stores different kinds of challenges, but the pattern is the same. """

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def get_challenge(self) -> tuple:
        return (self.question, self.answer)
    
    def get_question(self):
        return self.question
    
    def get_answer(self):
        return self.answer
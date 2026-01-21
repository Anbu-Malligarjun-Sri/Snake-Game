class Scientists:
    def __init__(self):
        self.occupation = "Scientists"
        self.job = "research"
        self.dream = "Nobel Price"

    def research(self):
        print("Let the research begin!")

class Physicists(Scientists):
    def __init__(self):
        super().__init__()

    def Reasearch_Field(self):
        super().research()
        print("Astronomy is the study of the universe.")


Richard_feynman = Physicists()
print("Occupation: ",Richard_feynman.occupation)
print("Dream",Richard_feynman.dream)
Richard_feynman.Reasearch_Field()
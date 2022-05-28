class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age:int, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, ch_name):
        self.name = ch_name
    
    def change_age(self, ch_age):
        self.age = ch_age

    def add_track(self, ch_track):
        self.tracks.append(ch_track)
    
    def get_score(self):
        print("{}'s score is {}".format(self.name, self.score))



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=31.64)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

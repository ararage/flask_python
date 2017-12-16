lottery_player_dict = {
    'name':'Rolf',
    'numbers':(5,9,12,3,1,21)
}
class LotteryPlayer:
    def __init__(self,name):
        self.name = name
        self.numbers = (5,9,12,3,1,21)
    def total(self):
        return sum(self.numbers)
        

player = LotteryPlayer("Rolf")
player.numbers = (5,9,12,3,1,21)
player2 = LotteryPlayer("John")
#print (player.name)
#print(player.total())

print(player.numbers == player2.numbers)

class Student:
    def __init__(self,name,school):
        self.name = name
        self.school = school
        self.marks = []
    def average(self):
        return sum(self.marks) / len(self.marks)
    @staticmethod
    def goToSchool():
        print ("I'm going to school")
    
anna = Student("Anna","MIT")
anna.marks.append(56)
anna.marks.append(16)

print (anna.average())
print(Student.goToSchool())
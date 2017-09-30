class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print("(Initializing {}".format(self.name))

        Robot.population += 1

    def die(self):
        print("{} is being destroyed".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} is the last one".format(self.name))
        else:
            print("There are still {:d} robots working".format(
                Robot.population))

    def say_hi(self):
        print("Greeting, my master call me {}".format(self.name))

    @classmethod
    def how_many(cls):
        print("we have {:d} robots".format(cls.population))

droid1 = Robot("001")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("002")
droid2.say_hi()
Robot.how_many()

print("Robots can do some work here")

print("Robots have finish their work")

droid1.die()
droid2.die()

Robot.how_many()

Robot.__doc__
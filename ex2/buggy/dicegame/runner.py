from .die import Die


class GameRunner:
    def __init__(self):
        self.dice = Die.create_dice(5)
        self.reset()

    def reset(self):
        self.round = 1
        self.wins = 0
        self.loses = 0

    def answer(self):
        total = 0
        for die in self.dice:
            total += die.value
        return total

    @classmethod
    def run(cls):
        # Probably counts wins or something.
        # Great variable name, 10/10.
        c = 0

        runner = cls()
        while True:
            runner.dice = Die.create_dice(5)
            print("Round {}\n".format(runner.round))

            for die in runner.dice:
                print(die.show())

            guess = input("Sigh. What is your guess?: ")

            while True:
                try:
                    guess = int(guess)
                    break
                except:
                    print('Please insert a number!')
                    guess = input("Sigh. What is your guess?: ")


            if guess == runner.answer():
                print("Congrats, you can add like a 5 year old...")
                runner.wins += 1
                c += 1
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                print("Like seriously, how could you mess that up")
                runner.loses += 1
                c = 0
            print("Wins: {} Loses {}".format(runner.wins, runner.loses))
            runner.round += 1

            if c == 6:
                print("You won... Congrats...")
                print("The fact it took you so long is pretty sad")
                break

            prompt = input("Would you like to play again?[Y/n]: ")

            # control input
            while True:
                if prompt == 'Y' or prompt == 'n':
                    break
                else:
                    print('Please insert Y eller n!')
                    prompt = input("Would you like to play again?[Y/n]: ")

            if prompt == 'Y':
                continue
            else:
                break






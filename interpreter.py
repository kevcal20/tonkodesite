
from textx import metamodel_from_file

class Ramen:

    def __init__(self):
        self.total_score = 0
        self.broth = None
        self.topping = None
        self.meat = None

        self.values = {
            'broth': {'tonkotsu': 65, 'miso': 35, 'shoyu': 20},
            'topping': {'tamago': 30, 'nori': 15, 'negi': 5},
            'meat': {'beef': 25, 'chashu': 50, 'chicken': 15}
        }

    def __str__(self):
        return (
            f"Broth: {self.broth}\n"
            f"Topping: {self.topping}\n"
            f"Meat: {self.meat}\n"
            f"Total Ramen Value: {self.total_score}"
        )

    def interpret(self, model):
        for cmd in model.selections:
            cmd_type = cmd.__class__.__name__

            if cmd_type == "BrothCommand":
                self.broth = cmd.type
                value = self.values['broth'][cmd.type]
                print(f"Adding broth: {cmd.type} ({value} points)")

            elif cmd_type == "ToppingCommand":
                self.topping = cmd.type
                value = self.values['topping'][cmd.type]
                print(f"Adding topping: {cmd.type} ({value} points)")

            elif cmd_type == "MeatCommand":
                self.meat = cmd.type
                value = self.values['meat'][cmd.type]
                print(f"Adding meat: {cmd.type} ({value} points)")

            else:
                print(f"Unknown command: {cmd_type}")
                continue

            self.total_score += value

        print("\nLets take it to the master for his approval!")
        print(f"\nRamen Master Rating: {self.total_score}")
        if self.total_score < 75:
            print("\nThat's a pretty bland bowl, I think you can do better!")
        elif self.total_score <= 99:
            print("\nYou're getting close! A little bit more and it will be perfect!")
        elif self.total_score == 100:
            print("\nThe perfect bowl!! You finally did it! You have now earned an apprenticeship in Japan!!")
        else:
            print("\nError: This ramen bowl is too powerful! Even the master couldn't handle it!")

ramen_mm = metamodel_from_file('ramen.tx')

ramen_model = ramen_mm.model_from_file('test6.ramen') 


ramen = Ramen()
ramen.interpret(ramen_model)
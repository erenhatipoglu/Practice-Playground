import pandas as pd
import random
import os
import platform

class God:
    def __init__(self, name, omnipotence, omniscience):
        self.name = name
        self.omnipotence = omnipotence
        self.omniscience = omniscience
        self.earthling = None

                                        # This one reads csv files as creation.
    def let_there_be(self, creation):
        if self.omnipotence:
            if creation.endswith(".csv") and os.path.exists(creation):
                self.earthling = pd.read_csv(creation)
                print(f"Let there be {creation}!")
                print(self.earthling.head())
                return self.earthling.head()
            else:
                return print(f"{self.name}: I only wanna read csv files!")
        else:
            print(f"{self.name} has no power here. He should be omnipotent")

                                        
                                        # Drops the target row in the dataset.
    def take_life(self, target_row):
        if self.omnipotence:
            if self.earthling is not None:
                if target_row in self.earthling.index:
                    self.earthling.drop(index=target_row, inplace=True)
                    print(f"Number {target_row} has been taken by God.")
                else:
                    print(f"{self.name}: No life can be taken before I create it first.")
        else:
            print(f"{self.name} has no power here. He should be omnipotent")


                                        # Gives one of the four prophecies randomly.
    def see_future(self):
        if self.omnipotence and self.omniscience:
            if self.earthling is not None:
                prophecies = [
                    "Ragnarok is near.",
                    "Those who sail west, will be rewarded.",
                    "Baldr's death is written in the chronicles of fate.",
                    "The battle will be lost, but the war will be won.",
                ]

                prophecy = random.choice(prophecies)
                print(f"{self.name} reveals a mystical prophecy: {prophecy}")
            else:
                print(f"{self.name} cannot see the future without a creation!")
        else:
            print(f"{self.name} has no power here. He should be omnipotent and omniscient")        


                                        # Resets the kernel and cleans the terminal.
    def doomsday(self):
        if self.omnipotence:
            if platform.system() == "Windows":
                os.system("cls")
            else:
                os.system("clear")

            print("Twilight of the Gods has ended and the world is born anew.")
        else:
            print(f"{self.name} has no power here. He should be omnipotent")

# Demonstration
Odin = God("Allfather", True, True)
Odin.let_there_be("iris.csv")
Odin.take_life(20)
Odin.see_future()
Odin.doomsday()

# Another God
Beelzebub = God("Lord of the Flies", True, False)
Beelzebub.let_there_be("mtcars.csv")
Beelzebub.take_life(25)
Beelzebub.see_future()
Beelzebub.doomsday()

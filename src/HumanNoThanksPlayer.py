from src.BaseNoThanksPlayer import BaseNoThanksPlayer


class HumanNoThanksPlayer(BaseNoThanksPlayer):
    def WillPass(self, boardState=None):
        while True:
            passInput = input("Pass (y / n): ").lower()
            if "y" in passInput:
                return True
            elif "n" in passInput:
                return False
            else:
                print("Incorrect input please give y, yes, no, or n")

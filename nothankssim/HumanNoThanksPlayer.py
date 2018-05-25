from nothankssim.BaseNoThanksPlayer import BaseNoThanksPlayer


class HumanNoThanksPlayer(BaseNoThanksPlayer):
    def willPass(self, boardState=None):
        passInput = None
        while passInput is None:
            passInput = input("Pass (Y/N): ")
            if "y" in passInput.lower():
                return True
            elif "n" in passInput.lower():
                return False
            else:
                print("In correct input please give y, yes, no, or n")

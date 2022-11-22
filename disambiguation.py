from difflib import SequenceMatcher


class Similarity:
    def __init__(self, text1, text2) -> None:
        self.text1 = text1
        self.text2 = text2
        self.ratio = SequenceMatcher(None, text1, text2).ratio()

    def __str__(self):
        return f"Similarity is {self.ratio}"

    def calculate(self) -> str:
        """Returns a name based on the similarity ratio
            A ratio greater than or equal to 0.7 is an apporximate match, if lower they are not similar

        Returns:
            str: Disambiguated name (first/second parameter)
        """
        self.ratio = round(self.ratio, 2)

        if self.ratio >= 0.7:
            return self.text1
        else:
            return self.text2


if __name__ == "__main__":

    print(
        """
  ______                           _      
 |  ____|                         | |     
 | |__  __  ____ _ _ __ ___  _ __ | | ___ 
 |  __| \ \/ / _` | '_ ` _ \| '_ \| |/ _ \\
 | |____ >  < (_| | | | | | | |_) | |  __/
 |______/_/\_\__,_|_| |_| |_| .__/|_|\___|
                            | |           
                            |_|           
"""
    )

    text1 = "This is a test string"
    text2 = "This is a test string 123"

    sim = Similarity(text1, text2)
    disambiguated_name = sim.calculate()

    print(f"Text 1: {text1}\nText 2: {text2}\nScore: {sim.ratio}")
    print(f"Output: {text2} -> {disambiguated_name}")

    print("\n", "*" * 20, "\n")

    name1 = "Tom Cruise"
    name2 = "Tom Cruise Jr"

    sim = Similarity(name1, name2)
    disambiguated_name = sim.calculate()

    print(f"Name 1: {name1}\nName 2: {name2}\nScore: {sim.ratio}")
    print(f"Output: {name2} -> {disambiguated_name}")

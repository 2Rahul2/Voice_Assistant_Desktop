import difflib
class similar:
    def __init__(self ,input_string):
        self.input_string = input_string
    def checkSimilar(self , reference_string , threshold):
        diff = difflib.ndiff(self.input_string , reference_string)
        diff_count = 0
        # print(diff)
        for line in diff:
            # print(line)
            # a "-", indicating that it is a deleted character from the input string.
            if line.startswith("-") or line.startswith("+"):
                diff_count += 1
        # calculates the similarity by subtracting the ratio of the number of deleted characters to the length of the input string from 1
        simliarNumber = 1 - (diff_count / len(reference_string))
        # print(simliarNumber)
        if simliarNumber > threshold:
            return True ,simliarNumber
        return False , simliarNumber
if __name__ == "main":
    s = similar('ambient.mp3')
    print(s.checkSimilar('ambient2.mp3' ,0.6))
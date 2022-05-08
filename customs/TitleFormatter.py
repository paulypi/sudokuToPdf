import re


class TitleFormatter:
    def letter_puzzle_titles(self, titles):
        """
        Get a list of two path in format str and return
        a string of titles formatted with spaces , on one line,
        to have the correct padding on a puzzle pdf page
        """
        if re.match(r"#[0-9]*.Easy$", titles[0][6:-4]):
            return " " * 25 + f'{titles[0][6:-4]}' + " " * 45 + f"{titles[1][6:-4]}"

        elif re.match(r"#[0-9]*.Medium$", titles[0][6:-4]):
            return " " * 23 + f'{titles[0][6:-4]}' + " " * 41 + f"{titles[1][6:-4]}"

        elif re.match(r"#[0-9]*.Hard$", titles[0][6:-4]):
            return " " * 25 + f'{titles[0][6:-4]}' + " " * 45 + f"{titles[1][6:-4]}"

    def letter_solution_titles(self, titles):
        """
        Get a list of three path in format str and return
        a string of titles formatted with spaces, on one line,
        to have the correct padding on a solution pdf page """
        return " " * 20 + f'{titles[0][6:-4]}' + " " * 35 + f"{titles[1][6:-4]}" + " " * 33 + f"{titles[2][6:-4]}"

    def run(self, titles: list, solution=None, format_="Letter"):
        """
        If the value of solution is True
        return a solution string otherwise return a puzzle string
        default value of solution is none.
        """
        # Implement different format
        if format_ == "Letter":
            if not solution:
                return self.letter_puzzle_titles(titles)
            else:
                return self.letter_solution_titles(titles)

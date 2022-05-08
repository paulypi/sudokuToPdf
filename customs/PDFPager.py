import re
from fpdf import FPDF
from customs.TitleFormatter import TitleFormatter


class Pager:
    """
    For puzzle:
        Create a pdf book with 4 sudoku per page,
        with a padded border as background and titles for every row of sudoku

    For solution:
        Create a pdf book with 9 sudoku per page,
        with a padded border as background and titles for every row of sudoku

    Format:
            A4		|	210 x 297 mm	|	8.3 x 11.7 in --not implemented
            Letter	|	216 x 279 mm	|	8.5 x 11.0 in
    """

    def __init__(self, format_="Letter"):
        self.format_ = format_
        self.width = 0
        self.x = 0
        self.y = 0
        self.pdf = FPDF()
        self.formatter = TitleFormatter()

    def format_title(self, title1, title2):
        # TODO: TO REMOVE
        if self.format_ == "A4":
            if re.match(r"#[0-9]*.Easy$", title1[6:-4]):
                if re.match(r"#[0-9]*.Easy$", title2[6:-4]):
                    return " " * 22 + f'{title1[6:-4]}' + " " * 42 + f"{title2[6:-4]}"
                elif re.match(r"#[0-9]*.Medium$", title2[6:-4]):
                    return " " * 22 + f'{title1[6:-4]}' + " " * 40 + f"{title2[6:-4]}"
                elif re.match(r"#[0-9]*.Hard$", title2[6:-4]):  # OK
                    return " " * 22 + f'{title1[6:-4]}' + " " * 43 + f"{title2[6:-4]}"

            if re.match(r"#[0-9]*.Medium$", title1[6:-4]):
                if re.match(r"#[0-9]*.Easy$", title2[6:-4]):
                    return " " * 20 + f'{title1[6:-4]}' + " " * 40 + f"{title2[6:-4]}"
                elif re.match(r"#[0-9]*.Medium$", title2[6:-4]):
                    return " " * 20 + f'{title1[6:-4]}' + " " * 37 + f"{title2[6:-4]}"
                elif re.match(r"#[0-9]*.Hard$", title2[6:-4]):
                    return " " * 20 + f'{title1[6:-4]}' + " " * 40 + f"{title2[6:-4]}"

            if re.match(r"#[0-9]*.Hard$", title1[6:-4]):
                if re.match(r"#[0-9]*.Easy$", title2[6:-4]):
                    return " " * 22 + f'{title1[6:-4]}' + " " * 43 + f"{title2[6:-4]}"
                elif re.match(r"#[0-9]*.Medium$", title2[6:-4]):
                    return " " * 22 + f'{title1[6:-4]}' + " " * 40 + f"{title2[6:-4]}"
                elif re.match(r"#[0-9]*.Hard$", title2[6:-4]):
                    return " " * 22 + f'{title1[6:-4]}' + " " * 43 + f"{title2[6:-4]}"

        if self.format_ == "Letter":
            if re.match(r"#[0-9]*.Easy$", title1[6:-4]):
                if re.match(r"#[0-9]*.Easy$", title2[6:-4]):
                    return " " * 22 + f'{title1[6:-4]}' + " " * 43 + f"{title2[6:-4]}"
                elif re.match(r"#[0-9]*.Medium$", title2[6:-4]):  # OK
                    return " " * 22 + f'{title1[6:-4]}' + " " * 40 + f"{title2[6:-4]}"
                elif re.match(r"#[0-9]*.Hard$", title2[6:-4]):  # OK
                    return " " * 22 + f'{title1[6:-4]}' + " " * 43 + f"{title2[6:-4]}"

            elif re.match(r"#[0-9]*.Medium$", title1[6:-4]):
                if re.match(r"#[0-9]*.Easy$", title2[6:-4]):
                    return " " * 20 + f'{title1[6:-4]}' + " " * 40 + f"{title2[6:-4]}"
                elif re.match(r"#[0-9]*.Medium$", title2[6:-4]):
                    return " " * 20 + f'{title1[6:-4]}' + " " * 37 + f"{title2[6:-4]}"
                elif re.match(r"#[0-9]*.Hard$", title2[6:-4]):
                    return " " * 20 + f'{title1[6:-4]}' + " " * 41 + f"{title2[6:-4]}"

            elif re.match(r"#[0-9]*.Hard$", title1[6:-4]):
                if re.match(r"#[0-9]*.Easy$", title2[6:-4]):
                    return " " * 22 + f'{title1[6:-4]}' + " " * 43 + f"{title2[6:-4]}"
                elif re.match(r"#[0-9]*.Medium$", title2[6:-4]):
                    return " " * 22 + f'{title1[6:-4]}' + " " * 41 + f"{title2[6:-4]}"
                elif re.match(r"#[0-9]*.Hard$", title2[6:-4]):
                    return " " * 22 + f'{title1[6:-4]}' + " " * 43 + f"{title2[6:-4]}"

            if re.match(r'Solution*', title1[6:-4]):
                return " " * 18 + f'{title1[6:-4]}' + " " * 30 + f"{title2[6:-4]}"

    def run(self, title_list, output_name):
        if len(title_list) > 3:
            if self.format_ == "A4":
                self.width = 210
                # HEIGHT = 297
                self.x = 0
                self.y = 40

                for i in range(int(len(title_list) / 4)):
                    title1, title2, title3, title4 = [title_list.pop(0) for _ in range(4)]
                    self.pdf.add_page(format="A4")
                    self.pdf.set_font('helvetica', '', 16)

                    self.pdf.image("A4_bg.jpg", 4, 25)  # test.jpg é il rettangolo di background
                    self.pdf.ln(15)
                    self.pdf.cell(self.x, self.y, self.format_title(title1, title2))

                    self.pdf.image(f"{title1}", 20, 48, int(self.width / 2 - 20), int(self.width / 2 - 20))
                    self.pdf.image(f"{title2}", int(self.width / 2), 48, int(self.width / 2 - 20),
                                   int(self.width / 2 - 20))
                    self.pdf.ln(120)

                    self.pdf.cell(self.x, self.y, self.format_title(title3, title4))

                    self.pdf.image(f"{title3}", 20, 168, int(self.width / 2 - 20), int(self.width / 2 - 20))
                    self.pdf.image(f"{title4}", int(self.width / 2), 168, int(self.width / 2 - 20),
                                   int(self.width / 2 - 20))

            if self.format_ == "Letter":
                self.width = 215.9
                # HEIGHT = 279.4
                self.x = 0
                self.y = 0

                # print(title_list[0][6:-4])

                if re.match(r"^#", title_list[0][6:-4]):
                    for i in range(int(len(title_list) / 4)):
                        title1, title2, title3, title4 = [title_list.pop(0) for _ in range(4)]

                        self.pdf.add_page(format="Letter")
                        self.pdf.set_font('helvetica', '', 16)

                        self.pdf.image("Letter_bg.jpg", 6, 8)  # test.jpg é il rettangolo di background
                        self.pdf.ln(20)
                        self.pdf.cell(int(self.x), int(self.y), self.formatter.run([title1, title2]))

                        self.pdf.image(f"{title1}", 17, 35, int(self.width / 2 - 20), int(self.width / 2 - 20))
                        self.pdf.image(f"{title2}", int(self.width / 2 + 2), 35, int(self.width / 2 - 20),
                                       int(self.width / 2 - 20))
                        self.pdf.ln(120)

                        self.pdf.cell(self.x, self.y, self.formatter.run([title3, title4]))

                        self.pdf.image(f"{title3}", 17, 155, int(self.width / 2 - 20), int(self.width / 2 - 20))
                        self.pdf.image(f"{title4}", int(self.width / 2 + 2), 155, int(self.width / 2 - 20),
                                       int(self.width / 2 - 20))

                elif re.match(r"^Solution*", title_list[0][6:-4]):
                    for i in range(int(len(title_list) / 9)):
                        title1, title2, title3, title4, title5, title6, title7, title8, title9 = [title_list.pop(0) for
                                                                                                  _ in range(9)]
                        self.pdf.add_page(format="Letter")
                        self.pdf.set_font('helvetica', '', 10)

                        self.pdf.image("Letter_bg.jpg", 6, 8)  # test.jpg é il rettangolo di background
                        self.pdf.ln(21)
                        self.pdf.cell(int(self.x), int(self.y),
                                      self.formatter.run([title1, title3, title2], solution=True))

                        self.pdf.image(f"{title1}", 17, 35, int(self.width / 3 - 16), int(self.width / 3 - 20))
                        self.pdf.image(f"{title3}", int(self.width / 3 + 13), 35, int(self.width / 3 - 20),
                                       int(self.width / 3 - 20))
                        self.pdf.image(f"{title2}", int(self.width / 3 + int(self.width / 3 + 5)), 35,
                                       int(self.width / 3 - 20), int(self.width / 3 - 20))
                        self.pdf.ln(77)

                        self.pdf.cell(self.x, self.y, self.formatter.run([title4, title6, title5], solution=True))

                        self.pdf.image(f"{title4}", 17, 112, int(self.width / 3 - 16), int(self.width / 3 - 20))
                        self.pdf.image(f"{title6}", int(self.width / 3 + 13), 112, int(self.width / 3 - 20),
                                       int(self.width / 3 - 20))
                        self.pdf.image(f"{title5}", int(self.width / 3 + int(self.width / 3 + 5)), 112,
                                       int(self.width / 3 - 20), int(self.width / 3 - 20))
                        self.pdf.ln(77)

                        self.pdf.cell(self.x, self.y, self.formatter.run([title7, title9, title8], solution=True))

                        self.pdf.image(f"{title7}", 17, 189, int(self.width / 3 - 16), int(self.width / 3 - 20))
                        self.pdf.image(f"{title9}", int(self.width / 3 + 13), 189, int(self.width / 3 - 20),
                                       int(self.width / 3 - 20))
                        self.pdf.image(f"{title8}", int(self.width / 3 + int(self.width / 3 + 5)), 189,
                                       int(self.width / 3 - 20), int(self.width / 3 - 20))
                        self.pdf.ln(50)

        self.pdf.output(f'{output_name}.pdf')

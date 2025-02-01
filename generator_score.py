


def generate_css(stroka, int_score):
    with open("output_score++.txt", "a", encoding="utf-8") as f:
        f.write(f""".c-column.user_rate[data-text*='✦: {stroka}'], .list-groups .b-table.list-lines tbody.entries tr[data-text*='✦: {stroka}'] {{
    order: -{int_score};
}}\n""")


def main():
    for score in range(1, 11):
        for elem in [["--", -4], ["-", -2], ["", 0], ["+", 2], ["++", 4]]:
            print(score, elem[0], elem[1])
            stroka = str(score)+elem[0]
            int_score = score * 10 + int(elem[1])
            generate_css(stroka, int_score)
main()

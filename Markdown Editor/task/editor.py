def print_unknown_formatting_message():
    print("Unknown formatting type or command")


def level_validation(level):
    while True:
        if level.isdigit() and 0 < int(level) < 6:
            return int(level)

        print("The level should be within the range of 1 to 6")
        level = input("- Level:")


def number_of_rows_validation(number):
    while True:
        if number.isdigit() and int(number) > 0:
            return int(number)

        print("The number of rows should be greater than zero")
        number = input("- Number of rows:")


def list_rows_input():
    number_of_rows = number_of_rows_validation(input("- Number of rows:"))
    rows = []
    for _ in range(number_of_rows):
        rows.append(input())
    return rows


def program():
    def plain_formatter():
        text = input("- Text:")
        formatted_text_list.append(text)

    def bold_formatter():
        text = input("- Text:")
        formatted_text_list.append(f'**{text}**')

    def italic_formatter():
        text = input("- Text:")
        formatted_text_list.append(f'*{text}*')

    def header_formatter():
        level = level_validation(input("- Level:"))
        text = input("- Text:")
        formatted_text_list.append(f"{'#' * level} {text}\n")

    def link_formatter():
        label = input("- Label:")
        url = input("- URL:")
        formatted_text_list.append(f'[{label}]({url})')

    def inline_code_formatter():
        text = input("- Text:")
        formatted_text_list.append(f'`{text}`')

    def ordered_list_formatter():
        rows = list_rows_input()
        formatted_text_list.append(''.join(map(lambda x: f"{rows.index(x) + 1}. {x}\n", rows)))

    def unordered_list_formatter():
        rows = list_rows_input()
        formatted_text_list.append(''.join(map(lambda x: f"* {x}\n", rows)))

    def new_line_formatter():
        formatted_text_list.append('\n')

    def print_help_message():
        print("Available formatters: "
              f"{' '.join(formatters)}"
              "\nSpecial commands: !help !done")

    def print_markdown_text():
        print(''.join(formatted_text_list))

    def save_to_file():
        with open('output.md', 'w') as result_file:
            result_file.writelines(formatted_text_list)
        result_file.close()

    def is_command_done(command):
        if command == '!done':
            save_to_file()
            return True

        if command == '!help':
            print_help_message()
            return False

        if command not in formatters:
            print_unknown_formatting_message()
            return False

        formatters[command]()
        return False

    def program_run():
        while True:
            if is_command_done(input("- Choose a formatter:")):
                break
            print_markdown_text()

    formatted_text_list = []

    formatters = {
        "plain": plain_formatter,
        "bold": bold_formatter,
        "italic": italic_formatter,
        "link": link_formatter,
        "inline-code": inline_code_formatter,
        "header": header_formatter,
        "ordered-list": ordered_list_formatter,
        "unordered-list": unordered_list_formatter,
        "new-line": new_line_formatter,
    }

    return program_run()


if __name__ == '__main__':
    program()

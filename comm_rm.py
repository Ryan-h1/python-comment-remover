import sys
from collections import deque


def remove_comments_dfa(source):
    """ This function removes all comments from the source code. """
    CODE = 0
    SINGLE_LINE_COMMENT = 1
    MULTI_LINE_COMMENT_SINGLE = 2
    MULTI_LINE_COMMENT_DOUBLE = 3
    STRING_SINGLE = 4
    STRING_DOUBLE = 5

    state = CODE
    parenthesis_stack = deque()  # Pseudo pushdown automaton to keep track of parentheses
    quote_stack = deque()  # Pseudo pushdown automaton to keep track of quotes
    cleaned_source = []

    i = 0

    # Check for and preserve shebang line if any
    if source.startswith("#!"):
        end_of_shebang = source.find('\n') + 1
        cleaned_source.append(source[:end_of_shebang])
        i = end_of_shebang  # Start processing the rest of the file after the shebang line

    while i < len(source):
        char = source[i]

        if state == CODE:
            # We are not checking for syntax errors here, so we assume that the parentheses are balanced
            if char in "([{":
                parenthesis_stack.append(char)
            elif char in ")]}":
                parenthesis_stack.pop()

            if len(parenthesis_stack) == 0:
                quote_stack.clear()

            if len(parenthesis_stack) > 0:
                # Logic for tracking quotes inside parentheses
                if char in "'\"":
                    if len(quote_stack) > 0 and quote_stack[-1] == char:
                        quote_stack.pop()
                    else:
                        quote_stack.append(char)
                # Logic for recognizing comments inside parentheses
                if char == '#' and len(quote_stack) == 0:
                    state = SINGLE_LINE_COMMENT
                else:
                    cleaned_source.append(char)
            elif char == '#':
                state = SINGLE_LINE_COMMENT
            elif char == "'" and source[i:i + 3] == "'''" and not_preceded_by_equals(source, i):
                state = MULTI_LINE_COMMENT_SINGLE
                i += 2  # Skip the next two quotes
            elif char == '"' and source[i:i + 3] == '"""' and not_preceded_by_equals(source, i):
                state = MULTI_LINE_COMMENT_DOUBLE
                i += 2  # Skip the next two quotes
            elif char == "'":
                state = STRING_SINGLE
                cleaned_source.append(char)
            elif char == '"':
                state = STRING_DOUBLE
                cleaned_source.append(char)
            else:
                cleaned_source.append(char)
        elif state == STRING_SINGLE:
            cleaned_source.append(char)
            # Check for an escaped quote
            if char == "'":
                backslash_count = 0
                j = i - 1
                while j >= 0 and source[j] == '\\':
                    backslash_count += 1
                    j -= 1
                if backslash_count % 2 == 0:  # Even number of backslashes means the quote is not escaped
                    state = CODE
        elif state == STRING_DOUBLE:
            cleaned_source.append(char)
            # Check for an escaped quote
            if char == '"':
                backslash_count = 0
                j = i - 1
                while j >= 0 and source[j] == '\\':
                    backslash_count += 1
                    j -= 1
                if backslash_count % 2 == 0:
                    state = CODE
        elif state == SINGLE_LINE_COMMENT:
            if char == '\n':
                state = CODE
                cleaned_source.append(char)
        elif state == MULTI_LINE_COMMENT_SINGLE:
            if char == '\n':
                cleaned_source.append(char)
            elif char == "'" and source[i:i + 3] == "'''" and source[i - 1] != '\\':
                state = CODE
                i += 2  # Skip the closing quotes
        elif state == MULTI_LINE_COMMENT_DOUBLE:
            if char == '\n':
                cleaned_source.append(char)
            elif char == '"' and source[i:i + 3] == '"""' and source[i - 1] != '\\':
                state = CODE
                i += 2  # Skip the closing quotes

        i += 1

    return ''.join(cleaned_source)


def not_preceded_by_equals(source, i):
    for j in range(i - 1, -1, -1):  # Start from i-1 and go backwards
        if source[j].isspace() or source[j] == '\\' or source[j] == '\n':  # backtrack
            continue
        return source[j] != '='
    return True


def main():
    if len(sys.argv) != 2:
        print("Usage: python comm_rm.py input_file.py")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = input_filename.rsplit('.', 1)[0] + '_rm.py'

    try:
        with open(input_filename, 'r', encoding='utf-8') as file:
            source_code = file.read()

        modified_source = remove_comments_dfa(source_code)

        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(modified_source)

        print(f"Comments removed. Output saved to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
        sys.exit(1)


if __name__ == "__main__":
    main()

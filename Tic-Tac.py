start_input = input()
groups_ammount = int(len(start_input) // 3)
char_by_char_list = [char for full_list in start_input for char in full_list]
char_by_groups_list = [char_by_char_list[ind:ind + groups_ammount] for ind in range(0, len(char_by_char_list), groups_ammount)]
final_result = ""

print("---------")
print("|", * char_by_groups_list[0], "|")
print("|", * char_by_groups_list[1], "|")
print("|", * char_by_groups_list[2], "|")
print("---------")

win_lines = [[inner_list[0] for inner_list in char_by_groups_list], [inner_list[1] for inner_list in char_by_groups_list], [inner_list[2] for inner_list in char_by_groups_list], * [inner_list for inner_list in char_by_groups_list], [char_by_groups_list[ind][ind] for ind in range(0, groups_ammount)], [char_by_groups_list[ind][(groups_ammount - 1) - ind] for ind in range(0, groups_ammount)]]

for inner_list in win_lines:
    if len([*[win_lines_inner for win_lines_inner in win_lines if win_lines_inner.count("X") == 3], * [win_lines_inner for win_lines_inner in win_lines if win_lines_inner.count("O") == 3]]) >= 2 or abs(char_by_char_list.count("X") - char_by_char_list.count("O")) > 1:
        final_result = "Impossible"
    elif len([*[win_lines_inner for win_lines_inner in win_lines if win_lines_inner.count("X") == 3]]) == 1:
        final_result = "X wins"
    elif len([*[win_lines_inner for win_lines_inner in win_lines if win_lines_inner.count("O") == 3]]) == 1:
        final_result = "O wins"
    elif len([*[win_lines_inner for win_lines_inner in win_lines if win_lines_inner.count("X") == 3], * [win_lines_inner for win_lines_inner in win_lines if win_lines_inner.count("O") == 3]]) == 0 and char_by_char_list.count("_") == 0:
        final_result = "Draw"
    elif len([*[win_lines_inner for win_lines_inner in win_lines if win_lines_inner.count("X") == 3], * [win_lines_inner for win_lines_inner in win_lines if win_lines_inner.count("O") == 3]]) == 0 and char_by_char_list.count("_") > 0:
        final_result = "Game not finished"

print(final_result)
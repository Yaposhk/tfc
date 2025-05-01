from math import inf

def translate_list(dic, vals):
    return [dic.get(x, "null") for x in vals]

def group_actions(actions):
    grouped = []
    if not actions:
        return grouped
    current_action = actions[0]
    count = 1
    for action in actions[1:]:
        if action == current_action:
            count += 1
        else:
            grouped.append(f"{current_action} x{count}")
            current_action = action
            count = 1
    grouped.append(f"{current_action} x{count}")
    return grouped

def find_hits(target):
    if target >= 0:
        coins = [2, 7, 13, 16, -3, -6, -9, -15]
        names = {
            2: "Штамповать", 7: "Изогнуть", 13: "Обжать", 16: "Усадить",
            -3: "Слабо ударить", -6: "Ударить", -9: "Сильно ударить", -15: "Протянуть"
        }
    else:
        coins = [-2, -7, -13, -16, 3, 6, 9, 15]
        names = {
            -2: "Штамповать", -7: "Изогнуть", -13: "Обжать", -16: "Усадить",
            3: "Слабо ударить", 6: "Ударить", 9: "Сильно ударить", 15: "Протянуть"
        }

    abs_target = abs(target)
    max_val = abs_target + max(abs(min(coins)), abs(max(coins))) + 1
    sol_len = [inf] * max_val
    sol_list = [[] for _ in range(max_val)]
    sol_len[0] = 0

    for i in range(max_val):
        for coin in coins:
            next_val = i + coin
            if 0 <= next_val < max_val and sol_len[next_val] > sol_len[i] + 1:
                sol_len[next_val] = sol_len[i] + 1
                sol_list[next_val] = sol_list[i] + [coin]

    if sol_len[abs_target] == inf:
        return "No solution exists"

    solution = sol_list[abs_target]
    solution.sort()
    return translate_list(names, solution)

if __name__ == "__main__":
    import sys
    target = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    result = find_hits(target)
    if isinstance(result, list):
        grouped = group_actions(result)
        print(", ".join(grouped))
    else:
        print(result)
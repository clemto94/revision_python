# GPT
def balancedOrNot(expressions, maxReplacements):
    result = []

    for expr, max_repl in zip(expressions, maxReplacements):
        stack = []
        replacements_needed = 0

        for char in expr:
            if char == '<':
                stack.append(char)
            elif char == '>':
                if stack:
                    stack.pop()
                else:
                    replacements_needed += 1

        if not stack and replacements_needed <= max_repl:
            result.append(1)
        else:
            result.append(0)

    return result


# Exemple d'utilisation
expressions = ['<<>>', '<>', '<><>', '>>', '<<>', '><><']
maxReplacements = [0, 1, 2, 2, 2, 2]
print(balancedOrNot(expressions, maxReplacements))  # Résultat attendu : [1, 1, 1, 1, 0, 0]


def balancedOrNot(expressions, maxReplacements):
    anwser = []
    for i in range(len(expressions)):
        ex = expressions[i]
        m_r = maxReplacements[i]
        count, nb_enter, nb_end = count_replace(ex)
        if ex[-1] == "<":
            anwser.append(0)
            continue
        if nb_enter > nb_end:
            anwser.append(0)
            continue
        if m_r == count:
            anwser.append(1)
            continue
        if m_r < count:
            anwser.append(0)
        elif m_r > 0 and count == 0:
            anwser.append(1)
        else:
            anwser.append(1)
        return anwser

# DeepSick

def balancedOrNotDeepSick(expressions, maxReplacements):
    results = []
    for expr, max_rep in zip(expressions, maxReplacements):
        balance = 0
        replacements_needed = 0
        for char in expr:
            if char == '<':
                balance += 1
            else:  # '>'
                if balance == 0:
                    replacements_needed += 1
                    balance += 1  # because we replace '>' with '<>', adding one '<'
                else:
                    balance -= 1
        # After processing all characters, balance should be zero and replacements_needed <= max_rep
        if balance == 0 and replacements_needed <= max_rep:
            results.append(1)
        else:
            results.append(0)
    return results
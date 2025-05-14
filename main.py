def main(words):
    re = {}
    for word in words:
        st = "".join(list(sorted(word)))
        if st in re:
            re[st].append(word)
            continue
        re[st] = [word]

    return [v for _, v in re.items()]

# [['listen', 'silent', 'enlist'], ['rat', 'tar', 'art'], ['hello'], ['world']]
if __name__ == '__main__':
    w = ["listen", "silent", "enlist", "rat", "tar", "art", "hello", "world"]
    r = main(w)
    print(r)
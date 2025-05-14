def stepping_cycle(iterable, step):
    buffer = []
    it = iter(iterable)
    idx = 0
    pos = 0

    while True:
        while len(buffer) <= (pos % max(1, len(buffer))):
            try:
                buffer.append(next(it))
            except StopIteration:
                if not buffer:
                    return
                break

        if not buffer:
            return

        current_index = pos % len(buffer)
        pass_num = (pos // len(buffer)) + 1
        yield (idx, pass_num, buffer[current_index])
        idx += 1
        pos += step


def count_replace(ex: str):
    count = 0
    enter = 0
    end = 0
    for s in ex:
        if s == '<':
            count += 1
            enter += 1
        if s == '>':
            count -= 1
            end += 1
    return count, enter, end


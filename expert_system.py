from fast_lemmas import SKIDKA, PERCENT, text2num_fast


def find_intervals(is_nums):
    prev = False
    intervals = []

    for e, x in enumerate(is_nums):
        if (prev is False) and (x is not None):
            start = e
            prev = True

        if (prev is True) and (x is None):
            stop = e
            prev = False
            intervals.append((start, stop))

    stop = len(is_nums)
    if prev is True:
        intervals.append((start, stop))
    return intervals


def expand_intervals_fast(intervals, words):
    processed_intervals = []

    for start, stop in intervals:
        if (stop < len(words)) and (words[stop] in PERCENT):
            stop += 1

        if (start > 0) and (words[start - 1] == "до"):
            start -= 1

        elif (start > 0) and (words[start - 1] == "в"):
            start -= 1
        processed_intervals.append((start, stop))
    return processed_intervals


def predict_example_fast(text, delta_skidka_left=2, delta_skidka_right=10):

    percent = set(["процента", "процентов", "процент", "проценты"])

    text = text.split()

    tmp_answer = ["O"] * len(text)
    for (
        i,
        word,
    ) in enumerate(text):

        if (word in SKIDKA) and (
            len(set(text[i - delta_skidka_left : i + delta_skidka_right + 1]) & percent)
            > 0
        ):

            sale_text = text[i - delta_skidka_left : i + delta_skidka_right + 1]
            is_num = [text2num_fast(x) for x in sale_text]
            intervals = find_intervals(is_num)
            intervals = expand_intervals_fast(intervals, sale_text)
            counter = 0
            for start, stop in intervals:
                if sale_text[stop - 1] not in PERCENT:
                    continue

                counter += 1

                if (
                    len(
                        set(
                            tmp_answer[
                                i
                                - delta_skidka_left
                                + start : i
                                - delta_skidka_left
                                + stop
                            ]
                        )
                        - set(["O"])
                    )
                    != 0
                ):
                    continue

                tmp_answer[i - delta_skidka_left + start] = "B-value"
                for x in range(start + 1, stop):
                    tmp_answer[i - delta_skidka_left + x] = "I-value"

                counter += 1
            if counter > 0:
                tmp_answer[i] = "B-discount"

    return tmp_answer

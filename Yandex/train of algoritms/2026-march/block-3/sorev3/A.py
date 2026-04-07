def grade(seq):
    vals = [ord(c) - ord("A") + 1 for c in seq]
    avg = sum(vals) / len(vals)
    round_res = int(avg + 0.5) if avg % 1 != 0.5 else int(avg)  # tie to smaller
    worst = max(vals)
    min_allowed = worst - 1
    final_val = max(
        round_res, min_allowed
    )  # if round_res is better (smaller) than min_allowed, use min_allowed
    return chr(final_val + ord("A") - 1)


print(grade(input().strip()))

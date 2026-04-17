n = int(input())
correct_answers = input().strip()
m = int(input())

students = [input().strip() for _ in range(m)]

similar_pairs = []

for i in range(m):
    for j in range(i + 1, m):
        ans_i = students[i]
        ans_j = students[j]

        correct_indices_i = [k for k in range(n) if ans_i[k] == correct_answers[k]]
        wrong_indices_i = [k for k in range(n) if ans_i[k] != correct_answers[k]]

        correct_indices_j = [k for k in range(n) if ans_j[k] == correct_answers[k]]
        wrong_indices_j = [k for k in range(n) if ans_j[k] != correct_answers[k]]

        correct_matches_i_to_j = sum(
            1 for k in correct_indices_i if ans_j[k] == ans_i[k]
        )
        wrong_matches_i_to_j = sum(1 for k in wrong_indices_i if ans_j[k] == ans_i[k])

        if (
            correct_matches_i_to_j > len(correct_indices_i) / 2
            and wrong_matches_i_to_j > len(wrong_indices_i) / 2
            and correct_matches_i_to_j > len(correct_indices_j) / 2
            and wrong_matches_i_to_j > len(wrong_indices_j) / 2
        ):
            similar_pairs.append((i + 1, j + 1))

print(len(similar_pairs))
for a, b in similar_pairs:
    print(a, b)

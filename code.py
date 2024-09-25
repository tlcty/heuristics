def generate_permutations(words):
    results = []

    def permute(arr, prefix=""):
        if len(arr) == 0:
            results.append(prefix.strip())
        else:
            for i in range(len(arr[0])):
                if arr[0][i]:
                    permute(arr[1:], f"{prefix} {arr[0][i]}")

    def generate_all_word_permutations(arr):
        if len(arr) == 0:
            return [[]]
        all_permutations = []

        for i in range(len(arr)):
            rest = arr[:i] + arr[i+1:]
            rest_permutations = generate_all_word_permutations(rest)

            for perm in rest_permutations:
                all_permutations.append([arr[i]] + perm)

        return all_permutations

    if isinstance(words, list) and len(words) > 0 and all(isinstance(item, list) for item in words):
        word_permutations = generate_all_word_permutations(words)

        for permutation in word_permutations:
            permute(permutation)
    else:
        print("Invalid input: words should be a non-empty list of lists.")

    return results

# Пример использования:
words = [
    ["System Analyst", "Системный аналитик", "System Аналитик"], 
    ["название команды", "(название команды)"],
    ["junior", "middle", "senior"]
]

permutations = generate_permutations(words)
print("\n".join(permutations))

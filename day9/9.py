def predict_right(values):
    if values[0] == 0 and values[-1] == 0:
        return 0
    differences = find_differences(values)
    return values[-1] + predict_right(differences)


def find_differences(values):
    differences = []
    for i in range(len(values) - 1):
        differences.append(values[i + 1] - values[i])
    return differences


if __name__ == "__main__":
    with open("day9/test.txt", "r") as file:
        lines = file.read().split("\n")
        acc = 0
        for line in lines:
            values = [int(value) for value in line.split(" ")]
            acc += predict_right(values)
        assert acc == 114
        print("Test 1 passed!")

        acc = 0
        for line in lines:
            values = [int(value) for value in line.split(" ")]
            acc += predict_right(values[::-1])
        assert acc == 2
        print("Test 2 passed!")

    with open("day9/input.txt", "r") as file:
        lines = file.read().split("\n")
        acc = 0
        for line in lines:
            values = [int(value) for value in line.split(" ")]
            acc += predict_right(values)
        print(f"Result part 1: {acc}")

        acc = 0
        for line in lines:
            values = [int(value) for value in line.split(" ")]
            acc += predict_right(values[::-1])
        print(f"Result part 2: {acc}")

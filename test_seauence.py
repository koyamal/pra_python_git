from typing import Any, Sequence, MutableSequence


def max_of(a: MutableSequence) -> Any:
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum


if __name__ == "__main__":
    x_list = [1, 5, 4, 6, 1, 5, 8, 9]
    x_tuple = (1, 5, 4, 6, 1, 5, 8, 9)

    print("List: ", max_of(x_list))
    print("tuple: ", max_of(x_tuple))  # MutableSequenceではない、タプルを引数に与えてもエラーは出ない

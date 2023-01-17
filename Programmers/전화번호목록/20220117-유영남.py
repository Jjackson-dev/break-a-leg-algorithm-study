def remove_min_nunber(numbers):
    min_number = min(numbers)
    # remove O(n), 정렬 후 pop 
    numbers.remove(min_number)
    return numbers, min_number


def solution(numbers):
    answer = True
    numbers.sort()
    min_number = numbers.pop()

    for phone_number in numbers:
        if min_number == phone_number[: len(min_number)]:
            answer = False
            break       
    return answer

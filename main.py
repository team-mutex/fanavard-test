#!/bin/python3


def main():
    # reading inputs
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))

    total_objects = 0  # number of objects we placed in boxes
    box_slots = k  # number of available slots in the current box

    # we process the objects in reverse order
    for i in reversed(a):
        # if we can't fit object in the box, we go to the next one
        if i > box_slots:
            box_slots = k
            m -= 1

        # when there is no more box left, we stop counting
        if m == 0:
            break

        box_slots -= i
        total_objects += 1

    print(total_objects)


if __name__ == '__main__':
    main()

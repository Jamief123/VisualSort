import pygame
import const
import sys
import threading
import time
from random import randint, seed, shuffle
from arg_parse import ArgParse

seed(1)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# initialize pygame
width = 600
height = 600
pygame.init()
screen_size = (width, height)


# clock is used to set a max fps
clock = pygame.time.Clock()
nums = []


def setup():
    # Draw the screen
    const.SCREEN = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("VisualSort")

    # Draw initial rectangles
    for num in nums:
        pygame.draw.rect(const.SCREEN, WHITE, [nums.index(num), height, 2, 0 - 0 - num], 0)
    pygame.display.update()
    # screen.fill(0)

    # Clear the numList so it does not stack every time this function is called
    nums.clear()
    for i in range(600):
        nums.append(i)
    shuffle(nums)


def update():
    for num in nums:
        pygame.draw.rect(const.SCREEN, WHITE, [nums.index(num), height, 2, 0 - 0 - num], 0)
    pygame.display.update()
    const.SCREEN.fill(0)


def swap(i, j):
    pygame.draw.rect(const.SCREEN, BLACK, [nums.index(nums[i]), height, 2, 0 - height], 0)
    pygame.draw.rect(const.SCREEN, BLACK, [nums.index(nums[j]), height, 2, 0 - height], 0)
    pygame.draw.rect(const.SCREEN, WHITE, [nums.index(nums[i]), height, 2, 0 - nums[i]], 0)
    pygame.draw.rect(const.SCREEN, WHITE, [nums.index(nums[j]), height, 2, 0 - nums[j]], 0)
    pygame.display.update()


def shell_sort(input_list):
    gap = len(input_list) // 2
    while gap > 0:

        for i in range(gap, len(input_list)):
            temp = input_list[i]
            j = i
            # Sort the sub list for this gap

            while j >= gap and input_list[j - gap] > temp:
                input_list[j] = input_list[j - gap]
                j = j - gap
            input_list[j] = temp
            update()

        # Reduce the gap for the next element

        gap = gap // 2


def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap(j, j + 1)  # this swap method updates the screen and has nothing to do with the algorithm


# ==============================QUICK SORT=============================================#

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    update()
    return (i + 1)


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quick_sort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# ====================================== END QUICK SORT==========================================#


def main():
    running = True
    thread = None
    parser = ArgParse()
    parser.parse_args()

    setup()

    if const.QUICKSORT:
        thread = threading.Thread(target=quick_sort, args=((nums, 0, len(nums)-1)),)
    elif const.BUBBLESORT:
        thread = threading.Thread(target=bubble_sort, args=(nums,))
    elif const.SHELLSORT:
        thread = threading.Thread(target=shell_sort, args=(nums,))
    else:
        parser.print_usage()
        running = False
        print('No option Selected. Select an algorithm')

    thread.start()

    while running:

        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        except(KeyboardInterrupt, SystemExit):
                running = False
                sys.exit()

        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()

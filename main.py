from tkinter import *
from tkinter import ttk
import random
from colors import *
import time

# Importing algorithms
from algorithms.bubbleSort import bubble_sort
from algorithms.selectionSort import selection_sort
from algorithms.insertionSort import insertion_sort
from algorithms.mergeSort import merge_sort
from algorithms.quickSort import quick_sort
from algorithms.heapSort import heap_sort
from algorithms.countingSort import counting_sort


# Main window
window = Tk()
window.title("Sorting Algorithms Visualization")
window.maxsize(5000, 1000)
window.config(bg=LIGHT_GRAY)

time_taken = StringVar()
algorithm_name = StringVar()
speed_name = StringVar()
array_name = StringVar()
data = []
algo_list = ['Bubble Sort', 'Insertion Sort', 'Selection Sort',
             'Merge Sort', 'Quick Sort', 'Heap Sort', 'Counting Sort']
speed_list = ['Fast', 'Medium', 'Slow']
array_list = ["10", '20', '50', '75', "100", '200']

# Drawing the numerical array as bars


def drawData(data, colorArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    window.update_idletasks()


# Randomly generate array
def generate():
    global data

    data = []
    for i in range(int(array_menu.get())):
        random_value = random.randint(1, int(array_menu.get()))
        data.append(random_value)

    drawData(data, [BLUE for x in range(len(data))])


def set_speed():
    if speed_menu.get() == 'Slow':
        return 0.3
    elif speed_menu.get() == 'Medium':
        return 0.1
    else:
        return 0.001


def sort():
    global data
    global time_taken
    timeTick = set_speed()
    start_time = time.time()

    if algo_menu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, timeTick)
        time_taken = time.time() - start_time
    elif algo_menu.get() == 'Selection Sort':
        selection_sort(data, drawData, timeTick)
        time_taken = time.time() - start_time
    elif algo_menu.get() == 'Insertion Sort':
        insertion_sort(data, drawData, timeTick)
        time_taken = time.time() - start_time
    elif algo_menu.get() == 'Merge Sort':
        merge_sort(data, 0, len(data)-1, drawData, timeTick)
        time_taken = time.time() - start_time
    elif algo_menu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, drawData, timeTick)
        time_taken = time.time() - start_time
    elif algo_menu.get() == 'Heap Sort':
        heap_sort(data, drawData, timeTick)
        time_taken = time.time() - start_time
    else:
        counting_sort(data, drawData, timeTick)
        time_taken = time.time() - start_time
    l4 = Label(UI_frame, text="Time taken to sort and visualize: " +
               str(time_taken), bg=WHITE, font=2, fg=YELLOW)
    l4.grid(row=4, column=2, padx=5, pady=5)
    # return time_taken


### User interface ###

def on_enter(e):
    e.widget['background'] = 'green'


def on_leave(e):
    e.widget['background'] = 'SystemButtonFace'


UI_frame = Frame(window, width=1500, height=600, bg=LIGHT_GRAY)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

l1 = Label(UI_frame, text="Algorithm: ", bg=LIGHT_GRAY)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(
    UI_frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

l2 = Label(UI_frame, text="Sorting Speed: ", bg=WHITE)
l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)

l3 = Label(UI_frame, text="Array size: ", bg=WHITE)
l3.grid(row=2, column=0, padx=10, pady=5, sticky=W)
array_menu = ttk.Combobox(UI_frame, textvariable=array_name, values=array_list)
array_menu.grid(row=2, column=1, padx=5, pady=5)
array_menu.current(0)

canvas = Canvas(window, width=800, height=400, bg=WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)

b1 = Button(UI_frame, text="Sort", command=sort, bg=LIGHT_GRAY)
b1.grid(row=3, column=1, padx=10, pady=10)
b1.bind("<Enter>", on_enter)
b1.bind("<Leave>", on_leave)

b3 = Button(UI_frame, text="Generate Array", command=generate, bg=LIGHT_GRAY)
b3.grid(row=2, column=2, padx=5, pady=5)


window.mainloop()

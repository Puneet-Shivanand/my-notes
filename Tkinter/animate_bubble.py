from Tkinter import *
import time
# don't pretend you're using lst, it's a bloody global!
# def bubbleSort(lst):
def bubbleSort():
    for number in range(len(lst)-1, 0, -1):
        for i in range(number):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                print lst
                animation()
                # let animcation handle these
                # cv.delete(ALL)
                # cv.update()

def animation():
    x , y = 200, 500
    barWidth = 15

    # this seems kind of pointless
    # you're about to delete all
    # for j in lst: cv.delete([j])
    cv.delete(ALL)
    for item in lst:
        # this is also pointless, you've deleted, leave it alone
        # cv.delete([item])  
        bar = cv.create_rectangle(x, y, x+barWidth, y-(item*15), fill="red")
        x += barWidth + 5
        # do this outside the loop
        # time.sleep(0.2)
        # cv.update()
    cv.update()
    time.sleep(0.2)
    
root = Tk() 
root.title("Bubble Sort")
w=600
h=700
cv = Canvas(width=w, height=h, bg='black')
cv.pack()
cv.update()

lst = [1,2,7,3,6,4,5,10,8,9,12,15,11,13,16,14,20,17,19,18]
bubbleSort()
root.mainloop()

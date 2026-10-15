- Date: 15/10
- Time: 16
- Length: 2
- Attended: Abdalla Victor Jai Omar Jamie Charlie Winston Tom
- Overview:
```
Sorted jobs and did some pseudocode
```
# Notes

JAI - HARDWARE
TOM - CAD
JAMIE - CAD
rest - 



prompt formatter-
networking-
servo-
pose
action doer+
teach doer+
action set mem
memory - whats where, tube description
main logic
json parser*
io


7




move3to5 = (pick up test3, move, put down in test5 if its empty)
centrifuge5_wait5 = (pick up 5, move to centrifuge, wait 5, pickup centruge, place in 5)

place in 5= (goto x y)









you are a lab assistant helper for gandling test tubes, please do the following:
INPUT
you must output it in the formatt of JSON
here are options:
Mode: Do, Teach
Do: runs an action
Teach: stores an action to memory
Action: a list of other actions

Available actions:
Goto(pos) goes to position specified
Pick
Place
Label: add description to a position


example formatt:
{Mode:DO,Action:[Pick,Place,Goto(tube3)]}




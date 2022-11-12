Exercise 8: Printing, Printing

We will now see how to do a more complicated formatting of a string. This code looks complex,
but if you do your comments above each line and break each thing down to its parts, you'll understand it.


Code ---->

-----------------------------------------------------------------------------------------------------------------------

formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))

-----------------------------------------------------------------------------------------------------------------------

What you will see

$ python3.6 ex8.py
1 2 3 4
one two three four
True False False True
{} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}
Try your Own text here Maybe a poem Or a song about fear

-----------------------------------------------------------------------------------------------------------------------

In this exercise I'm using something called a "function" to turn the formatter variable into other strings. When you see me write formatter.format(...) I'm telling python to do the following:

Take the formatter string defined on line 1.
Call its format function, which is similar to telling it to do a command line command named format.
Pass to format four arguments, which match up with the four {} in the formatter variable.
This is like passing arguments to the command line command format.
The result of calling format on formatter is a new string that has the {} replaced with the four variables.
This is what print is now printing out.
That's a lot for the eighth exercise, so what I want you to do is consider this a brain teaser.
It's alright if you don't really understand what's going on because the rest of the book will slowly make this clear.
At this point, try to study this and see what's going on, then move on to the next exercise.



Study Drills

Repeat the Study Drill from Exercise 7.
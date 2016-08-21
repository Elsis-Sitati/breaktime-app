import webbrowser
import time

total_breaks = 3
break_count = 0

# telling us when the programme began
print ('This programe started on ' + time.ctime())
# declaring for loop tto count three times
while(break_count <= total_breaks):

	# suspend the programme for 2 hours
	time.sleep(2*60*60)
	# opening the given url
	webbrowser.open("https://www.youtube.com/watch?v=1Vvkq2ts5q8")
	break_count = break_count + 1
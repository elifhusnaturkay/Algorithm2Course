'''
q = 7 // 3
print (q)

r = 7 % 3
print (r) 

response = input("What is your radius?")
print(type(response))

total_secs = int(input("How many seconds, in total? \n")) 
hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
minutes = secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining % 60
print("Hrs=", hours, "\nmins=", minutes,
     "\nsecs=", secs_finally_remaining)
'''


'''
Write a Python program that assigns the principal amount of $10000 to variable P, assign to n the value 12, and assign to r the interest rate of 8%. Then have the program prompt the user for the number of years t that the money will be compounded for.

Calculate and print the final amount after t years.

P = 10000
n = 12
r = 8/100
t = int(input("How many years will the money be compounded for?"))
A = P*(1+r/n) ** (n*t)
print("Final amount after", A, "years.")

'''

'''
#Q7-8:
You look at the clock and it is exactly 2pm. You set an alarm to go off in 51 hours. At what time does the alarm go off? (Hint: you could count on your fingers, but this is not what we’re after. If you are tempted to count on your fingers, change the 51 to 5100.)
'''

entrySnapTime = int(input("Saat kaç? : "))
entryTime = int(input("Alarm kaç saat sonra çalsın? : "))
days = entryTime // 24
hours = (entryTime % 24) + entrySnapTime
print("Alarmınız " + str(days) + " gün, " +str(hours) + " saat sonra çalacaktır.")



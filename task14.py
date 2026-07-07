#convert milliseconds to hours minutes and seconds
def time(millisecond):
    total_second = millisecond // 1000
    hour = total_second // 3600
    minutes = (total_second % 3600) // 60
    seconds = total_second % 60
    print(hour,"hour(s)",minutes,"minutes(s)",seconds,"second(s)")
millisecond = int(input("enter millisecondsn "))  
time(millisecond)  


    
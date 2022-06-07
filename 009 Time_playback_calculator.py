print('Enter time in h:m:s format.')
time_input = input("Enter time: ")

speed = float(input("\nEnter how fast/slow: "))

new_time_input = time_input.split(':')
new_time_input = [int(i) for i in new_time_input]

def secCalculator(s):
    sec_in_time = s
    return sec_in_time

def minCalculator(m,s):
    sec_in_min = m*60
    sec_in_time = s+ sec_in_min
    return sec_in_time

def hourCalculator(h,m,s):
    sec_in_hour = h*3600
    sec_in_min = m*60
    sec_in_time = s + sec_in_min + sec_in_hour
    return sec_in_time

def timeDividor(seconds):
    hrInSec = int(seconds/3600)
    new_seconds_1 = seconds - (hrInSec*3600)
    
    minInSec = int(new_seconds_1/60)
    new_seconds_2 = new_seconds_1 - (minInSec*60)
    
    remaining_sec = int(new_seconds_2)
    
    if seconds < 60:
        return '{} seconds'.format(remaining_sec)
    elif seconds >= 60 and seconds < 3600:
        return '{}m:{}s'.format(minInSec, remaining_sec)
    elif seconds >= 3600:
        return '{}:{}:{}'.format(hrInSec, minInSec, remaining_sec)
    
if len(new_time_input) == 1:
    time = secCalculator(new_time_input[0])
elif len(new_time_input) == 2:
    time = minCalculator(new_time_input[0], new_time_input[1])
elif len(new_time_input) == 3:
    time = hourCalculator(new_time_input[0],new_time_input[1],new_time_input[2])
else:
    print("Too much parameter.")

time = time/speed
finalTime = timeDividor(time)
print('Time will be reduced to {} from {} with {}x of speed.'.format(finalTime, time_input,speed))


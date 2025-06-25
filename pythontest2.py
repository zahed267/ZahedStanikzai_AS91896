import time
def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" %  (hour, minutes, seconds)

print("Press enter to start the stopwatch, and again to stop it.")
input() # use the input() function to wait for the user to press enter
print("stopwatch started")
start_time =time.time()
input()
print("stopwatch stopped")
end_time =time.time()
print("elasped time:", convert (end_time - start_time), "minutes")



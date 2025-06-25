import time

def stopwatch():
    print("Press enter to start the stopwatch")
    input()  # wait for user to press enter to start
    start_time = time.time()
    print("stopwatch has started. press enter to stop")
    input()  # wait for the user to click enter agian to stop
    end_time = time.time()


    elasped_time = end_time - start_time
    print(f"stopwatch stopped. elasped time: {elasped_time:.2f} seconds.")



    
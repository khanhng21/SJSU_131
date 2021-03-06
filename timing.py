import time
"""
Take a function to calculate the time to run the function
"""
def calculate_time(function):
    #take parameters and run function to get the run time of this fuction
    def timer(*args, **kw):
        start_time = time.time()
        x = function(*args, **kw)
        end_time = time.time()
        run_time = end_time - start_time
        print(float('Total time X: ',run_time))
        return x
    return timer
@calculate_time

def function():
    #test if it's correct
	time.sleep(2)
function()
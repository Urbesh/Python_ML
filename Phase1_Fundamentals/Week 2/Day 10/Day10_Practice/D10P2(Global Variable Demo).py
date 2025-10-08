'''
Global Variable Demo:
Create a counter that increments every time a function is called (use a global variable).
'''
call_count = 0
def count_function():
  global call_count 
  call_count += 1
  print(f"count_function has been called {call_count} time(s).")
  #Lets call the function for 3 times 
count_function()
count_function()
count_function()

print(f"The final call count is: {call_count}")

'''
Explanation:
call_count = 0: This line initializes a global variable named call_count to 0. 
Since it's defined outside any function, it has global scope.

def count_function(): This defines a function named as count_function.

global call_count: Inside my_function, this statement explicitly declares that the call_count being 
referred to within this function is the global variable, not a new local variable. 
This is crucial for modifying the global variable's value.

call_count += 1: This line increments the value of the global call_count by 1 
each time my_function is called.

print(...): This line prints a message indicating how many times the function has been called.

The subsequent calls to my_function() demonstrate the counter incrementing with each invocation.

Finally, printing call_count outside the function shows the final value of the global counter.
'''
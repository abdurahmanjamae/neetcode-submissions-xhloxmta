class MinStack:

    def __init__(self):
        # Main stack holds all pushed values
        self.stack = []
        # Min stack holds the running minimum at each position
        self.minStack = []
        

    def push(self, val: int) -> None:
        # Add the actual value to the main stack
        self.stack.append(val)

        # Compute the new minimum:
        # - If minStack is empty, the minimum is val
        # - Otherwise, compare val with the current minimum (last element)
        val = min(val, self.minStack[-1] if self.minStack else val)

        # Push the updated running minimum to minStack
        self.minStack.append(val)
        

    def pop(self) -> None:
        # Remove the top value from both stacks.
        # This works because minStack always mirrors stack in length.
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        # Return the top element of the main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # The top of minStack always stores the minimum so far
        return self.minStack[-1]

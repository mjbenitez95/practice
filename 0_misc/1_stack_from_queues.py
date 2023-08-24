TEST_CASES = [
    [[1,2,3,4,5,6], [6,5,4,3,2,1]],
    [[1,2,1,4,1,6], [6,1,4,1,2,1]],
    [[], []],
    [[1,100,1], [1,100,1]],
    [[2,100,1], [1,100,2]],
]

class MyStack:
    queue = []
    queue2 = []

    def push(self, num):
        self.queue.append(num)

    def pop(self):
        if len(self.queue2) == 0:
            if len(self.queue) == 0:
                return 
            
            while len(self.queue) != 0:
                self.queue2.append(self.queue.pop())

        return self.queue2.pop(0)

if __name__ == "__main__":
    for case in TEST_CASES:
        stack = MyStack()
        ans = []

        for num in case[0]:
            stack.push(num)
        
        for i in range(len(case[0])):
            ans.append(stack.pop())
            
        print(ans == case[1])


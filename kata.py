# 1
# Complete the function that takes a list of numbers (nums), as the only argument to the function.
# Take each number in the list and square it if it is even, or square root the number if it is odd.
# Take this new list and return the sum of it


def process_and_sum_numbers(nums):
    total = 0
    
    for num in nums:
        if num % 2 == 0:
            print("{0} is even".format(num))
            total += num ** 2
            print("total: {0}".format(total))
        elif num % 2 == 1:
            print("{0} is odd".format(num))
            total += num ** (1/2)
            print("total: {0}".format(total))

    return total


sum = process_and_sum_numbers([2, 5, 30, 10, 11000])
print(sum)

        


# 2
# YouTube had a like and a dislike button, which allowed users to express their opinions about particular content.
# It was set up in such a way that you cannot like and dislike a video at the same time.
# There are two other interesting rules to be noted about the interface: Pressing a button, which is already active, will undo your press.
# If you press the like button after pressing the dislike button, the like button overwrites the previous "Dislike" state.
# The same is true for the other way round.

# like_or_dislike([Dislike, Like, Like, Dislike, Like, Dislike, Dislike]) 
# like_or_dislike([Like, Like]) ➞ Nothing
# like_or_dislike([Dislike, Like]) ➞ Like
# like_or_dislike([Like, Dislike, Dislike]) ➞ Nothing

def like_or_dislike(like_or_dislike):
    state = "Nothing"
    
    for item in like_or_dislike:
        if item == "Like":
            
            if state == "Nothing" or state == "Dislike":
                print("Print flip to like")
                
                state = "Like"
            elif state == "Like":
                print("Print flip to nothing")
                state = "Nothing"
        
        elif item == "Dislike":
            print("Dislike")

            if state == "Dislike":
                print("Print flip to nothing")
                state = "Nothing"
            elif state == "Nothing" or state == "Like":
                print("Print flip to dislike")
                state = "Dislike"

    return state
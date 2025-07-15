# 4. Say a box of cookies can hold 24 cookies, and a container can hold 75 boxes of cookies. Write a program that prompts the user to enter the total number of cookies, then outputs the number of boxes and the number of containers to ship the cookies. Note that each box must contain the specified number of cookies, and each container must contain the specified number of boxes. If the last box of cookies contains less than the number of specified cookies, you can discard it and output the number of leftover cookies. Similarly, if the last container contains less than the number of specified boxes, you can discard it and output the number of leftover boxes

total_cookies = int(input("Enter total number of cookies: "))
cookies_per_box = 24
boxes_per_container = 75
boxes = total_cookies // cookies_per_box
leftover_cookies = total_cookies % cookies_per_box
containers = boxes // boxes_per_container
leftover_boxes = boxes % boxes_per_container
print(f"Total boxes: {boxes}")
print(f"Total containers: {containers}")
if leftover_cookies: print(f"Leftover cookies: {leftover_cookies}")
if leftover_boxes: print(f"Leftover boxes: {leftover_boxes}")
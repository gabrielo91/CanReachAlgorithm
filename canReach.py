def canReach(x1, y1, x2, y2):
    stack = []
    stack.append({"x1":x1, "y1":y1})
    
    while(len(stack)>0):
        points = stack.pop()
               
        x1 = points['x1']
        y1 = points['y1']
        
        if x1==x2 and y1==y2:
            return "Yes"
        elif x1 > x2 or y1 > y2:
            return "No"
        else:
            suma = x1+y1
            if suma <=x2:
                stack.append({"x1":suma, "y1":y1})
            if suma <=y2:
                stack.append({"x1":x1, "y1":suma})
    return "No"
    

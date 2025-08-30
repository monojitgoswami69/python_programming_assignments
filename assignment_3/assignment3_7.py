# 7. Write a function CityBusRoute() which will calculate the fare for passengers in City Bus Ring Route. A bus moves from station 1 to station 8 and then goes to station 1 and so on in ring format. The fare is the minimum distance between boarding and drop station multiplied by 5. The distance is calculated as |drop station - boarding station| if drop station > boarding station, else (8 - boarding station) + drop station (ring distance).

def CityBusRoute():
    boarding = int(input("Enter boarding station: "))
    drop = int(input("Enter drop station: "))
    
    if not (1 <= boarding <= 8) or not (1 <= drop <= 8):
        return "INVALID INPUT"
    
    if boarding == drop:
        return "No fare: Same station"
    
    clockwise = (drop - boarding) % 8
    anticlockwise = (boarding - drop) % 8
    
    min_distance = min(clockwise, anticlockwise)
    fare = min_distance * 5
    
    return fare

fare = CityBusRoute()
print(f"Fare: {fare}")

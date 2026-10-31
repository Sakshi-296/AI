
rooms = {
    "A": "Dirty",
    "B": "Dirty"
}

location = "A"

print("Initial Room Status:",rooms)


while True:

    if rooms[location] == "Dirty":
        print("\nLocation:", location)
        print("Percept:", location, "is Dirty")
        print("Action: SUCK")
        rooms[location] = "Clean"

    else:
        if location == "A":
            print("\nLocation:", location)
            print("Percept:", location, "is Clean")
            print("Action: Move Right")
            location = "B"
        else:
            print("\nLocation:", location)
            print("Percept:", location, "is Clean")
            print("Action: Move Left")
            location = "A"

    print("Current Room Status:", rooms)

    if rooms["A"] == "Clean" and rooms["B"] == "Clean":
        print("\nGoal Achieved!")
        print("Both rooms are clean.")
        break
# Bus Route Management System

# 1. Store bus routes in dictionary
bus = {
    "Durg": {"Bhilai": 10, "Raipur": 40, "Rajnandgaon": 45},
    "Bhilai": {"Durg": 10, "Raipur": 30},
    "Raipur": {"Bhilai": 30, "Bilaspur": 110, "Dhamtari": 80, "Durg": 40},
    "Bilaspur": {"Raipur": 110},
    "Dhamtari": {"Raipur": 80},
    "Rajnandgaon": {"Durg": 45},
    "Jagdalpur": {"Kondagaon": 75},
    "Kondagaon": {"Jagdalpur": 75}
}

# 2. Show connections of a stop
def show_connections(stop):

    if stop not in bus:
        print("Stop", stop, "not found.")
        return

    print(stop, "connects to:")

    for place, distance in bus[stop].items():
        print(place, "(", distance, "km )")


# 3. Find route using BFS
def find_route(start, end):

    if start not in bus or end not in bus:
        print("Invalid stop name.")
        return

    if start == end:
        print("Source and destination are the same.")
        print("Distance: 0 km")
        print("Fare: Rs. 0.00")
        return

    queue = [[start]]
    visited = [start]

    while queue:

        path = queue.pop(0)
        current = path[-1]

        if current == end:
            distance = 0

            for i in range(len(path) - 1):
                distance = distance + bus[path[i]][path[i + 1]]

            fare = distance * 1.50

            print("Route:", " -> ".join(path))
            print("Stops:", len(path))
            print("Distance:", distance, "km")
            print("Fare: Rs.", format(fare, ".2f"))
            return

        for place in bus[current]:

            if place not in visited:
                visited.append(place)
                new_path = path + [place]
                queue.append(new_path)

    print("No route available between", start, "and", end)


# 4. Main menu
while True:
    print("\n===== BUS ROUTE MANAGEMENT =====")
    print("1. Show Connections")
    print("2. Find Route")
    print("3. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        stop = input("Enter stop name: ")
        show_connections(stop)

    elif choice == "2":
        start = input("From: ")
        end = input("To: ")
        find_route(start, end)

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
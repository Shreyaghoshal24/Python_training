import csv

readDistance = csv.DictReader(open("Distance.csv"))
readRoute = csv.DictReader(open("Routes.csv"))
distances = {}

def calculateTotalDistance(stops, distances):
    totalDistance = 0

    for i in range(len(stops) - 1):
        currentStop = stops[i]
        nextStop = stops[i + 1]
        totalDistance += distances.get((currentStop, nextStop), 0)

    return totalDistance

def main():
    for row in readDistance:
        distances[(row['from'], row['to'])] = int(row['distance'])
        distances[(row['to'], row['from'])] = int(row['distance'])

    # print(distances)

    for row in readRoute:
        stops = row['stops'].split(', ')
        # print(stops)
        totalDistance = calculateTotalDistance(stops, distances)

        print(f"Total distance from {row['source']} to {row['destination']} via {stops}: {totalDistance} kilometers")

if __name__ == "__main__":
    main()

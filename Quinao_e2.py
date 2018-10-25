import sys

#input("Please put the Wind Intensity to identified what category it is.")

Wind = sys.argv[1]
Wind = float (Wind)

if Wind >= 220:
    print("Super Typhoon")
elif Wind >= 220:
    print("Typhoon")
elif Wind >= 89:
    print("Severe Tropical Storm")
elif Wind >=88:
    print("Tropical Storm")
elif Wind <=61:
    print("Tropical Depression")
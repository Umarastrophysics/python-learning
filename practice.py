mass = float(input("put mass in (solar masses) find type of cosmic body"))
if mass < 0.013:
    print("it is a rocky planet or a gas giant")
elif mass < 0.08:
    print("it is a brown drarf")
elif mass < 8:
    print("it is a small or medium star")
elif mass < 18:
    print("it will collapse into a neutron star")
elif mass >= 18:
    print("it will collapse into a black hole")
else:
    print("uknown cosmic object")

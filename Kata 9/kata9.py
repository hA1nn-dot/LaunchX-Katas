import numbers


def generateReport(mainTank, externalTank, hydrogenTank):
    totalAverge = mainTank + externalTank + hydrogenTank / 3
    return f"""Fuel Report:
    Total average: {totalAverge} %
    Main tank: {mainTank} %
    External tank: {hydrogenTank} %
    """
def average(values):
    total = sum(values)
    numItems = len(values)
    return total / numItems

#print(generateReport(12,52,32))

def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f'Total time to launch is {total_minutes} minutes'
    else:
        return f'Total time to launch is {total_minutes/60} hours'

#print(sequence_time(20,21,2))

def variable_length(**kwargs):
    return(kwargs)
#print(variable_length(tanks=1, day='Wednesday', pilots=3))

def mission_report(destination, *minutes, **fuel_reservoirs):
    main_report = f"""
    Mission to {destination}
    Total travel time: {sum(minutes)} minutes
    Total fuel left: {sum(fuel_reservoirs.values())}
    """
    for tank_name, gallons in fuel_reservoirs.items():
        main_report += f"{tank_name} tank --> {gallons} gallons left\n"    
    return main_report

print(mission_report("Moon", 8, 11, 55, main=300000, external=200000))
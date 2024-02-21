DayOfWeek = [
    # beginning, end, weekend
    [1,   0,   0  ],
    [1,   0,   0  ],
    [0.5, 0.5, 0  ],
    [0,   1,   0  ],
    [0,   0.8, 0.2],
    [0,   0,   1  ],
    [0,   0,   1  ],
]

Month = [
    # winter, spring, summer, autumn
    [1,   0,   0,   0  ],
    [1,   0,   0,   0  ],
    [0.6, 0.4, 0,   0  ],
    [0,   1,   0,   0  ],
    [0,   0.6, 0.4, 0  ],
    [0,   0,   1,   0  ],
    [0,   0,   1,   0  ],
    [0,   0,   1,   0  ],
    [0,   0,   0.8, 0.2],
    [0,   0,   0,   1  ],
    [0.8, 0,   0,   0.2],
    [1,   0,   0,   0  ],
]

def trapezoid(a, b, c, d):
    def func(x):
        if x <= a:
            return 0
        if x <= b:
            return (x - a) / (b - a)
        if x <= c:
            return 1
        if x <= d:
            return 1 - (x - c) / (d - c)
        return 0
    return func

def ramp_up(a, b):  # Not used yet, would be cleaner
    def func(x):
        if x <= a:
            return 0
        if x <= b:
            return (x - a) / (b - a)
        return 1
    return func

def ramp_down(c, d):  # Not used yet, would be cleaner
    def func(x):
        if x <= c:
            return 1
        if x <= d:
            return 1 - (x - c) / (d - c)
        return 0
    return func



lambda_functions = {
        'Month.winter': lambda x: Month[x['Month'] - 1][0],
        'Month.spring': lambda x: Month[x['Month'] - 1][1],
        'Month.summer': lambda x: Month[x['Month'] - 1][2],
        'Month.autumn': lambda x: Month[x['Month'] - 1][3],
        'DayOfMonth.beginning': lambda x: (
            trapezoid(1,1,9,13)(x['DayofMonth'])),
        'DayOfMonth.middle': lambda x: trapezoid(9,13,17,20)(x['DayofMonth']),
        'DayOfMonth.end': lambda x: trapezoid(17,20,31,31)(x['DayofMonth']),
        'DayOfWeek.beggining': lambda x: DayOfWeek[x['DayOfWeek'] - 1][0],
        'DayOfWeek.end': lambda x: DayOfWeek[x['DayOfWeek'] - 1][1],
        'DayOfWeek.weekend': lambda x: DayOfWeek[x['DayOfWeek'] - 1][2],
        'DepTime.morning': lambda x: (
            trapezoid(5.3,6.3,10.3,11.3)(x['DepTime'])),
        'DepTime.midday': lambda x: (
            trapezoid(10.3,11.3,13.3,14.0)(x['DepTime'])),
        'DepTime.afternoon': lambda x: (
            trapezoid(13.3,14.0,17.3,18.3)(x['DepTime'])),
        'DepTime.evening': lambda x: (
            trapezoid(17.3,18.3,22.3,23.0)(x['DepTime'])),
        'DepTime.night': lambda x: trapezoid(22.3,23.0,5.3,6.3)(x['DepTime']),
        'ArrTime.morning': lambda x: (
            trapezoid(5.3,6.3,10.3,11.3)(x['ArrTime'])),
        'ArrTime.midday': lambda x: (
            trapezoid(10.3,11.3,13.3,14.0)(x['ArrTime'])),
        'ArrTime.afternoon': lambda x: (
            trapezoid(13.3,14.0,17.3,18.3)(x['ArrTime'])),
        'ArrTime.evening': lambda x: (
            trapezoid(17.3,18.3,22.3,23.0)(x['ArrTime'])),
        'ArrTime.night': lambda x: trapezoid(22.3,23.0,5.3,6.3)(x['ArrTime']),
        'AirTime.veryShort': lambda x: trapezoid(0,0,60,90)(x['AirTime']),
        'AirTime.short': lambda x: trapezoid(60,90,160,200)(x['AirTime']),
        'AirTime.medium': lambda x: trapezoid(160,200,300,380)(x['AirTime']),
        'AirTime.long': lambda x: trapezoid(300,380,600,720)(x['AirTime']),
        'AirTime.veryLong': lambda x: (
            trapezoid(600,720,99999,99999)(x['AirTime'])),
        'ArrDelay.early': lambda x: (
            trapezoid(-99999,-99999,-1,0)(x['ArrDelay'])),
        'ArrDelay.onTime': lambda x: trapezoid(-1,0,2,4)(x['ArrDelay']),
        'ArrDelay.short': lambda x: trapezoid(2,4,6,8)(x['ArrDelay']),
        'ArrDelay.acceptable': lambda x: trapezoid(6,8,12,16)(x['ArrDelay']),
        'ArrDelay.long': lambda x: trapezoid(12,16,30,60)(x['ArrDelay']),
        'ArrDelay.veryLong': lambda x: (
            trapezoid(30,60,99999,99999)(x['ArrDelay'])),
        'DepDelay.none': lambda x: trapezoid(0,0,2,4)(x['DepDelay']),
        'DepDelay.short': lambda x: trapezoid(2,4,6,8)(x['DepDelay']),
        'DepDelay.acceptable': lambda x: trapezoid(6,8,12,16)(x['DepDelay']),
        'DepDelay.long': lambda x: trapezoid(12,16,30,60)(x['DepDelay']),
        'DepDelay.veryLong': lambda x: (
            trapezoid(30,60,99999,99999)(x['DepDelay'])),
        'Distance.veryShort': lambda x: trapezoid(0,0,100,200)(x['Distance']),
        'Distance.short': lambda x: trapezoid(100,200,400,700)(x['Distance']),
        'Distance.medium': lambda x: (
                trapezoid(400,700,1800,2200)(x['Distance'])),
        'Distance.long': lambda x: (
                trapezoid(1800,2200,3000,3800)(x['Distance'])),
        'Distance.veryLong': lambda x: (
                trapezoid(3000,3800,99999,99999)(x['Distance'])),
        'TaxiIn.short': lambda x: trapezoid(-1,-1,10,20)(x['TaxiIn']),
        'TaxiIn.medium': lambda x: trapezoid(10,20,40,60)(x['TaxiIn']),
        'TaxiIn.long': lambda x: trapezoid(40,60,400,400)(x['TaxiIn']),
        'TaxiOut.short': lambda x: trapezoid(-1,-1,10,20)(x['TaxiOut']),
        'TaxiOut.medium': lambda x: trapezoid(10,20,40,60)(x['TaxiOut']),
        'TaxiOut.long': lambda x: trapezoid(40,60,400,400)(x['TaxiOut']),
        'CarrierDelay.none': lambda x: trapezoid(0,0,2,4)(x['CarrierDelay']),
        'CarrierDelay.short': lambda x: trapezoid(2,4,6,8)(x['CarrierDelay']),
        'CarrierDelay.acceptable': lambda x: (
                trapezoid(6,8,12,16)(x['CarrierDelay'])),
        'CarrierDelay.long': lambda x: (
                trapezoid(12,16,30,60)(x['CarrierDelay'])),
        'CarrierDelay.veryLong': lambda x: (
                trapezoid(30,60,10000,10000)(x['CarrierDelay'])),
        'WeatherDelay.none': lambda x: trapezoid(-1,0,2,4)(x['WeatherDelay']),
        'WeatherDelay.short': lambda x: trapezoid(2,4,6,8)(x['WeatherDelay']),
        'WeatherDelay.acceptable': lambda x: (
                trapezoid(6,8,12,16)(x['WeatherDelay'])),
        'WeatherDelay.long': lambda x: (
                trapezoid(12,16,30,60)(x['WeatherDelay'])),
        'WeatherDelay.veryLong': lambda x: (
                trapezoid(30,60,10000,10000)(x['WeatherDelay'])),
        'SecurityDelay.none': lambda x: (
                trapezoid(-1,0,2,4)(x['SecurityDelay'])),
        'SecurityDelay.short': lambda x: (
                trapezoid(2,4,6,8)(x['SecurityDelay'])),
        'SecurityDelay.acceptable': lambda x: (
                trapezoid(6,8,12,16)(x['SecurityDelay'])),
        'SecurityDelay.long': lambda x: (
                trapezoid(12,16,30,60)(x['SecurityDelay'])),
        'SecurityDelay.veryLong': lambda x: (
                trapezoid(30,60,10000,10000)(x['SecurityDelay'])),
        'LateAircraftDelay.none': lambda x: (
                trapezoid(-1,0,2,4)(x['LateAircraftDelay'])),
        'LateAircraftDelay.short': lambda x: (
                trapezoid(2,4,6,8)(x['LateAircraftDelay'])),
        'LateAircraftDelay.acceptable': lambda x: (
                trapezoid(6,8,12,16)(x['LateAircraftDelay'])),
        'LateAircraftDelay.long': lambda x: (
                trapezoid(12,16,30,60)(x['LateAircraftDelay'])),
        'LateAircraftDelay.veryLong': lambda x: (
                trapezoid(30,60,10000,10000)(x['LateAircraftDelay'])),
}

import matplotlib.pyplot as plt
import math

# Que-2.1
def que21():
    # Weather of 2019-05-07
    # from https://weather.yahoo.co.jp/weather/jp/8/4020/8220.html
    tsukuba = [14, 13, 13, 16, 16, 13, 13, 12]

    # from https://weather.yahoo.co.jp/weather/jp/13/4410/13119.html
    itabashi = [15, 14, 14, 18, 19, 16, 15, 14]

    label_x = ["AM 0{}:00".format(time) for time in range(0, 12, 3)]
    label_x += ["PM 0{}:00".format(time) for time in range(0, 12, 3)]
    # print(label_x)

    plt.plot(label_x, tsukuba, itabashi)
    plt.legend(['Tsukuba', 'Itabashi'])
    plt.show()


# Que-2.2
def que22():
    xs = list(range(-10, 9))
    ys = [x ** 2 + 2 * x + 1 for x in xs]

    plt.plot(xs, ys)
    plt.show()


# Que-2.3
def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile motion of a ball')

def frange(start, final, interval):
    numbers = []

    while start < final:
        numbers.append(start)
        start += interval
    
    return numbers

def draw_trajectory(u, theta, i):
    theta = math.radians(theta)
    g = 9.8

    # Time of flight
    t_flight = 2 * u * math.sin(theta) / g

    # Find time intervals
    intervals = frange(0, t_flight, 0.001)

    # List of x and y coordinates
    x = []
    y = []

    for t in intervals:
        x.append(u * math.cos(theta) * t)
        y.append(u * math.sin(theta) * t - 0.5 * g * t ** 2)

    draw_graph(x, y)

    print('\n##### input {} #####'.format(i + 1))
    print('Flight time: {}s'.format(t_flight))
    print('Distance   : {}m'.format(x[-1]))
    print('Height     : {}m'.format(max(y)))

def input_values(us, ts):
    try:
        ans = int(input('How many trajectories? '))
    except ValueError:
        print('You entered an invalid input')
    else:
        for i in range(ans):
            try:
                u = float(input('Enter the initial velocity {} (m/s): '.format(i + 1)))
                theta = float(input('Enter the angle of projection {} (degrees): '.format(i + 1)))
            except ValueError:
                print('You entered an invalid input')
            else:
                us.append(u)
                ts.append(theta)

    return ans

def que23():
    us = []
    ts = []

    ans = input_values(us, ts)

    for i in range(ans):
        draw_trajectory(us[i], ts[i], i)

    plt.show()


# Que-2.4
def input_value24(ctgs, exps):
    try:
        category = input('Enter category: ')
        expend = int(input('Expenditure: '))
    except ValueError:
        print('You entered an invalid input')
    else:
        ctgs.append(category)
        exps.append(expend)

def input_values24():
    ctgs = []
    exps = []

    try:
        num = int(input('Enter the number of categories: '))
    except ValueError:
        print('You entered an invalid input')
    else:
        for i in range(num):
            input_value24(ctgs, exps)
    
    return (exps, ctgs)

def draw_pays(data, labels):
    num_bars = len(data)
    positions = range(1, num_bars + 1)

    # Create bar-graph
    plt.barh(positions, data, align='center')

    # Set labels
    plt.yticks(positions, labels)
    plt.xlabel('Categories')
    plt.ylabel('Amount')
    plt.title('Weekly expenditures')

    # Add grid-line
    plt.grid()

    plt.show()

def que24():
    (exps, ctgs) = input_values24()
    print(ctgs)
    print(exps)
    draw_pays(exps, ctgs)


# Que-2.5
def get_fibs(n):
    if n == 1:
         return [1]

    if n == 2:
        return [1, 1]

    a = 1
    b = 1
    series = [a, b]

    for i in range(n):
        c = a + b
        series.append(c)
        a = b
        b = c

    return series

def get_rates(series):
    rates = []

    for i in range(1, len(series)):
        rates.append(series[i] / series[i - 1])

    return rates

def que25():
    n = 100
    fibs = get_fibs(n)
    rates = get_rates(fibs)

    plt.plot(rates)
    plt.show()

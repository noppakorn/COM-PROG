def plot_map_info2(stations, names, date_time):
    lats  = [stations[name]['lat' ] for name in names]
    longs = [stations[name]['long'] for name in names]
    temps = [str(stations[name]['temp'])+'°c' for name in names]
    for i in range(len(temps)):
        print(names[i].title(), temps[i])

def test():
    while True:
        print("Weather Report:\n" +
              " (0) List all stations\n" +
              " (1) Temperatures at selected stations\n" +
              " (2) Top K max & min temperature stations\n" +
              " (3) Temperatures at the peak stations\n" +
              " (4) Temperatures at the nearby stations\n" +
              " (5) Average temperatures in the region")
        choice = input('Select 0,1,2,3,4,5: ')
        if '0' <= choice <= '5': break
        print('Try again.')

    date_time, names_in_region, stations = read_weather_data()
    names = []
    if choice == '0':
        show_all_station_names(stations)
    elif choice == '1':
        name = input("Station name: ")
        names = approx_match(stations, name)
        if len(names) == 0:
            print('No', name, 'in database.')
    elif choice == '2':
        k = int(input("K: "))
        names = top_k_min_temp_stations(stations, k)
        names.extend(top_k_max_temp_stations(stations, k))
    elif choice == '3':
        names = peak_stations(stations)
    elif choice == '4':
        main_station = input("Main station: ").strip().upper()
        if main_station not in stations:
            print('No ' + main_station + ' in database')
        else:
            k = int(input("How many nearby stations? "))
            names = [main_station] + k_nearby_stations(stations, main_station, k)
    elif choice == '5':
        region = input("Region (N,E,W,S,C,NE): ").strip().upper()
        if region not in names_in_region:
            print('Invalid region')
        else:
            names = names_in_region[region]
            avg_temp = average_temp(stations, names)
            print('Average temperature =', str(round(avg_temp,1)) + '°c')

    if len(names) > 0: plot_map_info2(stations, names, date_time)

test()
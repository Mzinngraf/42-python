def ft_count_harvest_recursive():
    days = int(input("Enter number of days: "))

    def count_days(current, days):
        if current > days:
            print("Harvest time!")
            return
        print(f"Day {current}")
        count_days(current + 1, days)
    count_days(1, days)

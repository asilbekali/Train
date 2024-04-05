class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def minute_count(self):
        return self.hour * 60 + self.minute

    def add_10_minutes(self):
        total_minutes = self.minute_count() + 10
        self.hour = total_minutes // 60
        self.minute = total_minutes % 60

class Train:
    def __init__(self, num_train, route, departure_time):
        self.num_train = num_train
        self.route = route
        self.departure_time = departure_time

    def display_info(self):
        print("\n\nPoyezd raqami:", self.num_train)
        print("Poyezd yo'nalishi:", self.route)
        print("Poyezning jo'nash vaqti:", self.departure_time.hour, "soat", self.departure_time.minute, "daqiqa", self.departure_time.second, "soniya")

trains = []
for i in range(5):
    train_num = int(input(f"Poyezd {i+1} raqamini kiriting: "))
    route = input(f"Poyezd {i+1} yo'nalishini kiriting: ")
    hour, minute, second = map(int, input(f"Poyezd {i+1} jo'nash vaqti (soat:daqiqa:soniya) ni kiriting: ").split(":"))
    departure_time = Time(hour, minute, second)
    train = Train(train_num, route, departure_time)
    trains.append(train)

current_hour, current_minute, current_second = map(int, input("Hozirgi vaqtni (soat:daqiqa:soniya) kiriting: ").split(":"))
current_time = Time(current_hour, current_minute, current_second)

train_num = int(input("Poyezd raqamini kiriting: "))

for train in trains:
    if train.num_train == train_num:
        train.display_info()
        remaining_minutes = (train.departure_time.minute_count() - current_time.minute_count()) % (24 * 60)
        remaining_hours = remaining_minutes // 60
        remaining_minutes %= 60
        print("Jonash vaqti:", remaining_hours, "soat", remaining_minutes, "daqiqa qoldi")

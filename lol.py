class Aeroplan:
    def __init__(self, Place = " - ", Number = " - ", Type = " - ", Time = " - ", Day = " - ", Cost = " - "):
        self.Place = Place
        self.Number = Number
        self.Type = Type
        self.Time = Time
        self.Day = Day
        self.Cost = Cost
    def Mesta(self):
        print("Стандартное количество мест: ", 200)
    def print_reyce_for_place(self, Reyce_list, place):
        print("Пункт назначения рейса{}:", format(place))
        for reyce in Reyce_list:
          if reyce.Place == place:
           print(reyce.Place, reyce.Number, reyce.Type, reyce.Time, reyce.Day)
    def print_day_for_reyce(self, reyce_list, day):
        print("Рейсы вылетающие в {}: ", format(day))
        for reyce in reyce_list:
          if reyce.Day == day:
            print(reyce.Place, reyce.Number, reyce.Type, reyce.Time, reyce.Day)
class Razryad(Aeroplan):
    def prise(self, reyce_list):
        for reyce in reyce_list:
         if reyce.Cost > 1000:
          print("Рейс с удобствами: ", reyce.Place, reyce.Number, reyce.Type, reyce.Time, reyce.Day, "Бизнес класс")
         else:
          print("Стандартный рейс: ", reyce.Place, reyce.Number, reyce.Type, reyce.Time, reyce.Day, "эконом класс")
    def Mesta(self, reyce_list):
        for reyce in reyce_list:
         if reyce.Cost > 1000:
          print("Места в бизнес классе: ", 50)
        else:
          print("Стандартное количество мест: ", 200)

reyce_1 = Aeroplan("Осло", 132, "Пассажирский", "12:30", "Вторник", 1500)
reyce_2 = Aeroplan("Осло", 234, "Пассажирский", "09:00", "Суббота", 900)
reyce_3 = Aeroplan("Нью-Йорк", 567, "Грузовой", "15:30", "Четверг", 700)
reyce_4 = Aeroplan("Лос-Анджелес", 874, "Пассажирский", "11:00", "Четверг", 1200)
reyce_5 = Razryad("Астана", 254, "Пассажирский", "14:20", "Пятница", 500)
reyce_6 = Razryad("Сан Хосе", 465, "Пассажирский", "15:50", "Понедельник", 1600)
Reyce_list1 = [reyce_1, reyce_2, reyce_3, reyce_4, reyce_5, reyce_6]
Reyce_list2 = [reyce_5, reyce_6]
show = Aeroplan()
show.Mesta()
show.print_reyce_for_place(Reyce_list1, "Осло")
show.print_day_for_reyce(Reyce_list1, "Четверг")
snow = Razryad()
snow.Mesta(Reyce_list2)
snow.prise(Reyce_list1)



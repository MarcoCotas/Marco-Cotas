months= {
    "January": 1,
    "February":2,
    "March": 3,
    "April": 4,
    "May":5 ,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12,
}
m,d,y = 0, 0 ,0
while True:
    date = input("Date: ").replace("/", ".").replace(",", "").strip()
    print (date)
    m, d, y = date.split(".")

    d = int(d)
    y = int(y)
    if d > 31:
        continue
    else:

        if m in months or m.isdigit() and int(m) in months.values():
            if m in months:
                month_number = months[m]
            else:
                month_number = int(m)
            print(f"{y}-{month_number:02}-{int(d):02}")
            break

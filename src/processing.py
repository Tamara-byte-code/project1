def filter_by_state(my_list, state="EXECUTED"):
    new_list = []
    for i in my_list:
        if i.get("state") == state:
            new_list.append(i)
    return new_list


def sort_by_date(my_list, sort_revers = True):
    return sorted(my_list, key = lambda i: i["date"], reverse= sort_revers)



if __name__ == '__main__':

    d = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

   # print(filter_by_state(d, "CANCELED"))
    print(*sort_by_date(d), sep="\n")


with open("olympics.txt","r") as filename:
    lines = filename.readlines()
    header = lines[0]
    field_names = header.strip().split(",")
    print(field_names)
    for row in lines[1:]:
        values = row.strip().split(",")
        record = dict(zip(field_names, values))
        print(record)
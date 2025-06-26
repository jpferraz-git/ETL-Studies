import json
import csv

from urllib3.filepost import writer

txt_data = "I like pizza!"

json_data = {
    "name": "John",
    "age": 43,
    "is_poor": True
}

csv_data = ["Eugene", "Squidward", "Spongebob", "Patrick"]

csv_test =[["Name", "Age", "Job"],
           ["Spongebob", 30, "Cook"] ,
           ["Patrick", 45, "Unmeployed"],
           ["Sandy", 23, "Scientist"]]

file_path = "output.txt"

path_place = "/home/user/ETL-Studies/ETL-Studies/output.csv"

with open(file=path_place, mode="w", newline="", ) as file:
    # for value in csv_data:
    #     file.write(value + "\n")

    writer = csv.writer(file)
    for row in csv_test:
        writer.writerow(row)

    # json.dump(json_data, file, indent=4)

    print(f"txt file {path_place} was created")

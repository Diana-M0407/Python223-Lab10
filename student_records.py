
# Diana Maldonado
# May 04, 2025
# Homework-Lab10: CSV Student Records

from collections import Counter
from pathlib import Path
from typing import List
import os, csv

class Records:
    def __init__(self, filename: str)-> None:
        self.filename:str = filename
        #self.data = List[Tuple[int, str, str]] = []
        #self.data = List[Dict[str, Union[int, str]]] = []
        self.data = []

    def load_csv(self)-> List[dict[int, str,str]]:
        if not os.path.exists(self.filename):
            raise FileNotFoundError(f"No such file: {self.filename!r}")

        with open(self.filename, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            # convert reader to a list of dicts
            self.data = list(reader)
            #print(self.data)

            # each row is a dict: {header1: value1, header2: value2, header3: value3}
        #for id_str, str_1, str_2 in self.data:
        #for row in self.data:
                # e.g. {'id': '152', 'level': 'SOPH', 'Major': 'CPSCI '}
         #   print(row)
         #   print(f"{id_str}, {str_1}, {str_2}")
                #self.data.append((int(id_str), str_1, str_2))
        return self.data
    
    def get_levels(self, levels: List[dict[str, int]])->List[dict[str, int]]:
        grade_levels = (row["Level"] for row in levels)
        return grade_levels

    def add_courses(self, ID: int, Total_Units: int, CPSC_Units: int, filename: str)-> bool:
        
        row = {
            "ID"          : ID,
            "Total Units" : Total_Units,
            "CPSC Units"  : CPSC_Units,
            }
        
        filename.append(row)

        with open(filename, "w", encoding= "utf-8") as f:
           fieldnames = ["ID", "Total Units", "CPSC Units"]
           writer = csv.writer(f, fieldnames = fieldnames)
           writer.writerheader()
           writer.writerow(self.data)
            
        return True    
    
    def get_units_per_student(self, courses: List[dict[str, str]])-> List[dict[str, int]]:
        unique_ids = list(dict.fromkeys(row["ID"] for row in courses))
        #count_ids = Counter(unique_ids)

        units_per_student: List[dict[str, int]] = []

        for id in unique_ids:
            tot_units = 0
            cs_units = 0
            for row in courses:
                #print(id)
                if row["ID"] == id:
                    #print(row)
                    tot_units += int(row['Units'])
                    if row["Course"].startswith("CPSC"):
                    #if row['Course'][:4] == "CPSC":
                        cs_units += int(row['Units'])
            student= {
                "ID":id, 
                "Total Units": tot_units, 
                "CPSC Units": cs_units
                }
            
            units_per_student.append(student)
        #print(units_per_student)
            #courses.save_to(id, total_units,CS_units,file)
            #print(f"{id}: total units: {total_units}, CPSCI units: {CPSCI_units}")
        return units_per_student


    def save_to(self, in_file:List[dict[str, int]], out_filename: str) -> None:
        with open(out_filename, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            # (optional) write a header row if you want
            writer.writerow(["ID", "Total Units", "CPSC Units"])

            # write each dict as a simple list of values
            for row in in_file:
                writer.writerow([
                    row["ID"],
                    row["Total Units"],
                    row["CPSC Units"],
                ])
        return None
   
    def print_levels(self, std_levels:List[dict[str, int]])-> None:
        counts = Counter(std_levels)
        print(f"{"="*15}")
        print(f"{counts['FRESH']} freshmen")
        print(f"{counts['SOPH']} sophmores")
        print(f"{counts['JR']} juniors")
        print(f"{counts['SR']} seniors", end="\n\n")
    
        return None
    
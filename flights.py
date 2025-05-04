# Diana Maldonado
# April 29, 2025
# Lab09- Tuffy Flight Schedule

from __future__ import annotations
import json
import re
from pathlib import Path
from typing import List, Tuple

_TIME_RE = re.compile(r"(?:[01]\d|2[0-3])[0-5]\d")

class Flights:
    def __init__(self, filename: str) -> None:
        self.filename: str = filename
        self.data: List[dict[str, str]] = []
        #list_of_flight_schedule = []

        try:

            # open file
            with open(self.filename, "r", encoding="utf-8") as f:
                #copy file into list
                self.data = json.load(f)
                if not isinstance(self.data, list):
                    self.data = []
        
        except FileNotFoundError:
            # No file found. File will be created on first add_flight() call.
            self.data = []

        except json.JSONDecodeError:
            self.data = []
    
    # Helper function
    @staticmethod
    def _verify_time(hhmm: str) -> bool:
        #returns True if time format is correct
        return bool(_TIME_RE.fullmatch(hhmm))

    def add_flight(self, origin: str, destination: str, flight_number: str, departure: str , next_day: str, arrival:str)-> bool:
        #origin        = origin
        #destination   = destination
        #flight_number = flight_number

        if not self._verify_time(departure):
            return False

        if not self._verify_time(arrival):
            return False
        
        if next_day not in ("Y", "N", "y", "n"):
            return False
        
        self.data.append(  
            {
            "origin"       : origin.upper(),
            "destination"  : destination.upper(),
            "flight_number": flight_number.upper(),
            "departure"    : departure,
            "next_day"     : next_day.upper(),
            "arrival"      : arrival,
            }
        )

        with open(self.filename, "w", encoding= "utf-8") as f:
            json.dump(self.data, f, indent=2)
            
        # return true if flight added and json written
        return True

    # Helper functions: 
    @staticmethod
    def _HHMM_to_minutes(HHMM: str):
        return int(HHMM[:2])*60 + int(HHMM[2:])
    
    @staticmethod
    def _minutes_to_HHMM(mins: int):
        h, m = divmod(mins, 60)
        return f"{h}:{m:02d}"
    
    @staticmethod
    def _format_ampm(HHMM: str):
        h, m = int(HHMM[:2]), int(HHMM[2:])
        ampm = "am" if h < 12 else "pm"
        h12 = h % 12 or 12
        return f"{h12}:{m:02d}{ampm}"
    
    def get_flights(self):
        display : list[tuple[str, str, str, str, str, str]] = []

        for f in self.data:
            depart_ampm = self._format_ampm(f["departure"])
            arrival_plus = f["next_day"] == "Y"
            arrival_ampm = ("+" if arrival_plus else '') + self._format_ampm(f["arrival"])

            mins = self._HHMM_to_minutes(f["arrival"]) - self._HHMM_to_minutes(f["departure"])
            if arrival_plus:
                mins += 24*60
            dur = self._minutes_to_HHMM(mins)

            display.append(
                (
                f["origin"],
                f["destination"],
                f["flight_number"],
                depart_ampm, arrival_ampm, dur,
                )
            )

        return display







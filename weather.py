import random
from datetime import datetime, timedelta

class WeatherStation:
    def __init__(self):
        self.data = []

    def collect_data(self):
        now = datetime.now()
        day_name = now.strftime("%A")
        reading = { 
            "temperature": round(random.uniform(15.0, 35.0), 2),
            "humidity": round(random.uniform(30.0, 90.0), 2),
            "timestamp": now.isoformat(),
            "day": day_name
        }
        self.data.append(reading)
        return reading
    
    def get_data_by(self):
        day_data = {}
        for r in self.data:
            day = r["day"]
            if day not in day_data:
                day_data[day] = []
            day_data[day].append(r["temperature"])
        
        avg_day_data = {}
        for day, temps in day_data.items():
            avg_day_data[day] = round(sum(temps) / len(temps), 2)
        return avg_day_data

    
    def average_temperature(self):
        if not self.data:
            return None
        all_temps = [r["temperature"] for r in self.data]
        return round(sum(all_temps) / len(all_temps), 2)
    
    def simulate_past_days(self, days=7):
        for i in range(days):
            day_time = datetime.now() - timedelta(days=i)
            day_name = day_time.strftime("%A")
            for _ in range(random.randint(1, 5)):
                reading = {
                    "temperature": round(random.uniform(15.0, 35.0), 2),
                    "humidity": round(random.uniform(30.0, 90.0), 2),
                    "timestamp": day_time.isoformat(),
                    "day": day_name
                }
                self.data.append(reading)
    
    def summary(self):
        return {
            "temperatures_by_day": self.get_data_by(),
            "average_temperature": self.average_temperature(),
        }
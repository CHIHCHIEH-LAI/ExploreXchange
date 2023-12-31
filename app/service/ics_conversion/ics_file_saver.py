import ics

class ICSFileSaver:
    def save(self, ics_data: ics.Calendar, file_path: str) -> None:
        with open(file_path, 'w') as trip_file:
            trip_file.writelines(ics_data)
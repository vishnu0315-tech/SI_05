from datetime import datetime

class Employee:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.attendance = []  # List to store attendance logs
    
    def clock_in(self):
        clock_in_time = datetime.now()
        self.attendance.append({"clock_in": clock_in_time, "clock_out": None})
        print(f"{self.name} clocked in at {clock_in_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    def clock_out(self):
        if not self.attendance or self.attendance[-1]["clock_out"] is not None:
            print("You must clock in first!")
            return
        clock_out_time = datetime.now()
        self.attendance[-1]["clock_out"] = clock_out_time
        print(f"{self.name} clocked out at {clock_out_time.strftime('%Y-%m-%d %H:%M:%S')}")

    def calculate_working_hours(self):
        total_hours = 0
        for log in self.attendance:
            if log["clock_out"]:
                time_diff = log["clock_out"] - log["clock_in"]
                total_hours += time_diff.total_seconds() / 3600  # Convert seconds to hours
        return total_hours
    
    def view_attendance(self):
        print(f"\nAttendance for {self.name}:")
        for log in self.attendance:
            clock_in = log["clock_in"].strftime('%Y-%m-%d %H:%M:%S')
            clock_out = log["clock_out"].strftime('%Y-%m-%d %H:%M:%S') if log["clock_out"] else "Still working"
            print(f"Clock-in: {clock_in}, Clock-out: {clock_out}")

class AttendanceSystem:
    def __init__(self):
        self.employees = {}

    def add_employee(self, employee_id, name):
        if employee_id not in self.employees:
            self.employees[employee_id] = Employee(employee_id, name)
            print(f"Employee {name} added successfully.")
        else:
            print(f"Employee with ID {employee_id} already exists.")
    
    def mark_attendance(self, employee_id, action):
        if employee_id not in self.employees:
            print("Employee not found!")
            return
        
        employee = self.employees[employee_id]
        if action == "in":
            employee.clock_in()
        elif action == "out":
            employee.clock_out()
        else:
            print("Invalid action. Use 'in' to clock in or 'out' to clock out.")

    def view_employee_attendance(self, employee_id):
        if employee_id not in self.employees:
            print("Employee not found!")
            return
        
        employee = self.employees[employee_id]
        employee.view_attendance()

    def calculate_employee_working_hours(self, employee_id):
        if employee_id not in self.employees:
            print("Employee not found!")
            return
        
        employee = self.employees[employee_id]
        total_hours = employee.calculate_working_hours()
        print(f"{employee.name} worked a total of {total_hours:.2f} hours.")
    
def main():
    system = AttendanceSystem()
    
    # Add employees
    system.add_employee(101, "Alice")
    system.add_employee(102, "Bob")
    
    # Mark attendance for employees
    system.mark_attendance(101, "in")
    system.mark_attendance(101, "out")
    
    system.mark_attendance(102, "in")
    system.mark_attendance(102, "out")
    
    # View individual attendance
    system.view_employee_attendance(101)
    system.view_employee_attendance(102)
    
    # Calculate total working hours
    system.calculate_employee_working_hours(101)
    system.calculate_employee_working_hours(102)

if __name__ == "__main__":
    main()

from fastapi import FastAPI
import uvicorn

app = FastAPI()

employees = {
    1: {"name": "Shreya", "l_name": "Ghoshal", "Doj": 2021}
}
employee_id_counter = 2


@app.get("/get_employees")
def get_employees():
    return employees


@app.post("/add_employee")
def add_employee(employee_data: dict):
    global employee_id_counter
    employee_id = employee_id_counter
    employees[employee_id] = employee_data
    employee_id_counter += 1
    return {"message": "Employee added successfully", "employee_id": employee_id, "employee_data": employee_data}


@app.put("/update_employee/{employee_id}")
def update_employee(employee_id: int, employee_data: dict):
    if employee_id in employees:
        employees[employee_id].update(employee_data)
        return {"message": "Employee updated successfully", "employee_id": employee_id, "employee_data": employee_data}
    else:
        return {"error": "Employee not found"}


@app.delete("/delete_employee/{employee_id}")
def delete_employee(employee_id: int):
    if employee_id in employees:
        deleted_employee = employees.pop(employee_id)
        return {"message": "Employee deleted successfully", "deleted_employee": deleted_employee}
    else:
        return {"error": "Employee not found"}


if __name__ == "__main__":
    uvicorn.run("test:app", host="127.0.0.1", port=8000, reload=True)

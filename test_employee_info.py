import employee_info

def test_calculate_average_salary():
    result=[]
    input_arr=[50000,60000,56000,70000,65000,60000]
    test_arr=60166.666666666664
    result=employee_info.calculate_average_salary()
    assert result == test_arr

def test_get_employees_by_dept():
    input_arr=[]
    test_arr= [{"name": "John", "age": 30, "department": "Sales", "salary": 50000},{"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
]
    input_arr=employee_info.get_employees_by_dept("Sales")
    assert (input_arr == test_arr)

def test_get_employees_by_age_range():
    input_arr=[]
    test_arr= [ {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},{"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]
    input_arr=employee_info.get_employees_by_age_range(24,38)
    assert(input_arr==test_arr)
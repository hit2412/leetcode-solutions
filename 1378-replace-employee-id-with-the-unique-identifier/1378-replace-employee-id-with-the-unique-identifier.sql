select u.unique_id, e.name
from Employees e
LEFT JOIN employeeUNI u on e.id=u.id

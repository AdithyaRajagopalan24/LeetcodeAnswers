with n1 as (
    select e.name as employee, salary, d.name as department, 
    dense_rank() over(partition by departmentId order by salary desc) as ranked 
    from employee e
    join department d
    on e.departmentId = d.id
)
select department, employee, salary from n1
where ranked <= 3;
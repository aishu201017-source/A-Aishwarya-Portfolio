SELECT 
    Gender,  
    COUNT(Gender) AS TotalCount,
    COUNT(Gender) * 100.0 / (SELECT COUNT(*) FROM Customer_Data) AS Percentage
FROM Customer_Data
GROUP BY Gender;


SELECT
    Contract,
    COUNT(Contract) as TotalCount,
    COUNT(Contract)*100.0/(SELECT COUNT(*) FROM Customer_Data) AS Percentage
FROM Customer_Data
GROUP BY Contract

Select
    Customer_Status,
    Count(Customer_Status) as TotalCount,
    Count(Customer_Status)*100.0/(Select Count(*) From Customer_Data) AS Perc_of_Total_Customers,
    Sum(Total_Revenue) as Revenue,
    Sum(Total_Revenue)*100.0/(Select Sum(Total_Revenue) From Customer_Data) As Revenue_Perc
From Customer_Data
Group By Customer_Status;


Select
    State,
    Count(State) as TotalCount,
    Count(State)*100.0/(Select Count(*) From Customer_Data) As Percentage
From Customer_Data
Group By State
Order By Percentage desc


Select Distinct Internet_Type
From Customer_Data

Select 
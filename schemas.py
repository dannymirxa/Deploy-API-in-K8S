from pydantic import BaseModel

"""
Which employee has the highest total sales amount (invoice total) to customers they support? The final result should show the employee's full name and their total sales.

SeLeCT e.first_name , e.last_name , SUM(i.Total) AS TotalSales 
	FROM employee AS e 
		JOIN customer AS c ON e.employee_id  = c.support_rep_id  
		JOIN invoice AS i ON c.customer_id  = i.customer_id  
	GROUP BY e.first_name , e.last_name  ORDeR BY TotalSales DeSC
"""

class EmployeeHighestSalesGet(BaseModel):
    first_name: str
    last_name: str
    TotalSales: float

    class Config:
        orm_mode = True


"""Which artists have albums that include tracks with the genre 'Rock'? The query should return a unique list of artist names.

SELECT DISTINCT Ar."name"  FROM artist AS Ar 
	JOIN album AS Al ON Ar.artist_id  = Al.artist_id 
	JOIN track AS T ON Al.album_id  = T.album_id 
	JOIN genre AS G ON T.genre_id  = G.genre_id 
		WHERE G."name" = 'Rock' ORDER BY Ar."name" ;
"""

class AristwithAlbumbyGenrePost(BaseModel):
    name: str

    class Config:
        orm_mode = True


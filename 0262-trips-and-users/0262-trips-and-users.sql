# Write your MySQL query statement below
SELECT
    Trips.request_at AS Day,
    ROUND(
        AVG(Trips.status <> 'completed'),
        2
    ) AS 'Cancellation Rate'
FROM Trips
JOIN Users Client
ON Trips.client_id = Client.users_id
JOIN Users Driver
ON Trips.driver_id = Driver.users_id
WHERE Client.banned = 'No'
  AND Driver.banned = 'No'
  AND Trips.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY Trips.request_at;
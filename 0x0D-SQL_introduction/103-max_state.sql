-- import from https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql
-- display the max temperature of each state (ordered by State name)

SELECT state, MAX(value) as 'max_temp' FROM temperatures GROUP BY state ORDER BY state;


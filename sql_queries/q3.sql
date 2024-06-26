### question 3
### Is there a correlation between two specific columns? Explain your findings.

select country_region,
    sum(confirmed) as total_metric
from covid19_project.public_transformed_layer.transform_covid19_data tcd 
group by country_region
order by total_metric desc;

### With the data I have, I am unable to use the corr function (correlation function of postgresql) that requires 2 integers to compare.
### But with the query above we can see that there is a correlation between the country and how many confirmed cases it has had.
### It may be due to the population size, culture of how the people delt and viewed covid 19, and the government's preparations or actions towards the pandemic.

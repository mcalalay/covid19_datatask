### question 1
### What are the top 5 most common values in a particular column, and what is their frequency?

select country_region, sum(confirmed) as frequency
from covid19_project.public_transformed_layer.transform_covid19_data tcd 
group by country_region
order by frequency desc
limit 5;

### I ranked the countr_region column looking to see how much confirmed cases there were per country and 
### to see who had the most confirmed cases throughout the pandemic.
### The leading country was US with 53,813,184,406 confirmed cases followed by India with 29,131,119,694
### followed by the Brazil with 21,182,690,594 followed by France with 16,105,911,886
### and lastly Germany with 13,868,043,710 confirmed cases.
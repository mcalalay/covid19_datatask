### question 2
### How does a particular metric change over time within the dataset?

select date_trunc('month', date) as month,
    sum(confirmed) as total_metric
from covid19_project.public_transformed_layer.transform_covid19_data tcd 
group by date_trunc('month', date)
order by month;

### I used the date and confirmed cases column to see how the pandemic evolved in months of its presence.
### If this were to be plotted in a graph or a BI tool, it would be very similar to an exponential graph 
### due to its exponential growth pattern, rising incredibly fast and topping of at around 20 Billion. 
### After which it start decreasing as time passes.
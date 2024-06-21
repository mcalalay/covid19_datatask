with raw_data as (
    select * from {{ ref('covid19_data') }}
),

transformed_data as (
    select
        "Province/State" as province_state,
        "Country/Region" as country_region,
        "Lat" as latitude,
        "Long" as longitude,
        cast("Date" as date) as date,
        cast("Confirmed" as int) as confirmed
    from raw_data
)

select * from transformed_data

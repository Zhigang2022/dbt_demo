{{ config( 
	materialized='view',
	schema='dbt'
)}}

with tbl as(
select "movieId", title, string_to_array(genres,'|') genres
from {{ ref('movies_pull') }}
),
tbl_flatten as(
select "movieId",title, unnest(genres) genre
from tbl
	)
select count(*) N, genre
from tbl_flatten
group by genre
order by N desc

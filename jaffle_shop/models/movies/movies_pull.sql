{{config(
	materialized='table',
	schema='dbt')
}}



select *
from {{ source('movies','movies') }}



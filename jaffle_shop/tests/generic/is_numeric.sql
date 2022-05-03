{% test is_numeric(model, column_name) %}

with tbl as(
	select 
	case when {{ column_name }} ~E'^\\d+$' then movieid::int
		else null
		end int_col
	from {{ model }}
)
select *
from tbl
where int_col is null

{% endtest %}

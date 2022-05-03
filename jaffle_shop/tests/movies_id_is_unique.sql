with tbl as(
	select count(*) cnt_id
	from public_dbt.movies_pull
	group by movieid
)
select * from tbl
where cnt_id>1

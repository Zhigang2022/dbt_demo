{% snapshot movies_snapshot %}

{{config(
    target_schema='snapshot',
    strategy='check',
    unique_key="genre",
    check_cols=['genre',]
)}}

select * from {{ ref('movies_cnt')}}

{% endsnapshot %}

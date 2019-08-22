SELECT
  t.table_name

FROM
  information_schema.tables t

WHERE
  1 = 1
  AND t.table_schema = 'poker_version2'
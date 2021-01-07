SELECT
  NVL(MAX(g.id), 0) AS max_id

FROM
  {database}.games g
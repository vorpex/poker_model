SELECT
  NVL(MAX(d.id), -1) AS max_id

FROM
  {database}.decision_points d
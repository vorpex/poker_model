SELECT
  SUM(CASE WHEN g1.position - g2.position = 1 OR (g1.position = 0 AND g2.position = 5) THEN 0 ELSE 1 END) AS checksum_result

FROM
  {database}.games g1

INNER JOIN
  {database}.games g2
ON
  g1.id + 1 = g2.id
  AND g1.uuid = g2.uuid
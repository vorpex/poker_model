SELECT
  SUM(CASE WHEN w.winner_stack = g.final_stack THEN 0 ELSE 1 END) AS checksum_result

FROM
  {database}.winners w

LEFT JOIN
  {database}.games g
ON
  w.game_id = g.id
  AND w.uuid = g.uuid
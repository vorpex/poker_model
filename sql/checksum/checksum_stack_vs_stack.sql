SELECT
  SUM(g.stack - t.starting_stack) AS checksum_result

FROM (

  SELECT
    h.game_id,
    h.uuid,
    MAX(h.stack) AS starting_stack

  FROM
    {database}.history h

  GROUP BY
    h.game_id,
    h.uuid

) t

INNER JOIN
  {database}.games g
ON
  t.game_id = g.id
  AND t.uuid = g.uuid
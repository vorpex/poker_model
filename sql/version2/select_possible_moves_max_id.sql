SELECT
  NVL(MAX(p.id), -1) AS max_id

FROM
  poker_version2.possible_moves p

WHERE
  1 = 1
  AND p.decision_point_id = {decision_point_id}
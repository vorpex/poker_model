SELECT
  NVL(MAX(p.id), -1) AS max_id

FROM
  poker.possible_moves p

WHERE
  1 = 1
  AND p.decision_point_id = {DECISION_POINT_ID}
SELECT
  p.id,
  p.move,
  p.amount,
  p.expected_value

FROM
  poker_version2.possible_moves p

WHERE
  1 = 1
  AND p.decision_point_id = {DECISION_POINT_ID}
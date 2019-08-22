SELECT
  p.id,
  p.action,
  p.amount,
  p.expected_value

FROM
  poker_version2.possible_moves p

WHERE
  1 = 1
  AND p.decision_point_id = {decision_point_id}
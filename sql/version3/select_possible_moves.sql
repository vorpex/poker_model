SELECT
  p.id,
  p.action,
  p.bet_amount_range,
  p.expected_value

FROM
  {database}.possible_moves p

WHERE
  1 = 1
  AND p.decision_point_id = {decision_point_id}

ORDER BY
  p.id
SELECT
  p.counter,
  p.total_profit

FROM
  {database}.possible_moves p

WHERE
  1 = 1
  AND p.decision_point_id = {decision_point_id}
  AND p.action = '{action}'
UPDATE
  poker_version2.possible_moves p

SET
  p.counter = {counter},
  p.total_profit = {total_profit},
  p.expected_value = {expected_value}

WHERE
  1 = 1
  AND p.decision_point_id = {decision_point_id}
  AND p.action = '{action}'
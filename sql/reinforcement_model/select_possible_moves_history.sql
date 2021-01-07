SELECT
  s1.uuid,
  s1.decision_point_id,
  s1.id,
  s1.h_action,
  s1.h_amount,
  s1.p_action,
  s1.p_amount,
  s1.counter,
  s1.total_profit,
  s2.stack,
  s2.final_stack,
  s2.profit

FROM (

  SELECT
    h.uuid,
    h.action AS h_action,
    h.amount AS h_amount,
    p.action AS p_action,
    p.bet_amount_range AS p_amount,
    p.decision_point_id,
    p.id,
    p.counter,
    p.total_profit

  FROM
    {database}.history h

  INNER JOIN
    {database}.decision_points d
  ON
    h.phase = d.phase
    AND h.nr = d.nr

  INNER JOIN
    {database}.possible_moves p
  ON
    d.id = p.decision_point_id
    AND h.action = upper(p.action)

  WHERE
    1 = 1
    AND h.game_id = {index}

) s1

INNER JOIN (
    
  SELECT
    g.uuid,
    g.stack,
    g.final_stack,
    g.final_stack - g.stack AS profit

  FROM
    {database}.games g

  WHERE
    1 = 1
    AND g.id = {index}

) s2
ON
  s1.uuid = s2.uuid

WHERE
  1 = 1
  AND ((s1.h_action = 'CALL' AND s1.p_action = 'call')
   OR (s1.h_action = upper(s1.p_action) AND s1.h_amount = s1.p_amount))

ORDER BY
  s1.decision_point_id,
  s1.id
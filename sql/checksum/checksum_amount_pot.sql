SELECT
  SUM(t.check_amount_pot) AS checksum_result

FROM (

  SELECT
    h.game_id,
    MAX(h.new_pot) - SUM(h.amount) AS check_amount_pot

  FROM
    {database}.history h
  
  GROUP BY
    h.game_id

) t
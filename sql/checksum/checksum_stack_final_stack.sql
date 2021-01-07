SELECT
  SUM(t.check_stack_final_stack) AS checksum_result

FROM (

  SELECT
    CASE
      WHEN g1.final_stack <= 2 * g1.small_blind_amount AND (g2.stack - g1.final_stack) MOD 2000 = 0 THEN 0
      ELSE g1.final_stack - g2.stack
    END check_stack_final_stack

  FROM
    {database}.games g1

  INNER JOIN
    {database}.games g2
  ON
    g1.id + 1 = g2.id
    AND g1.uuid = g2.uuid

) t
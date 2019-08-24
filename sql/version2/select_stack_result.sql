SELECT
  g.stack - g.final_stack AS stack_result

FROM
  poker_version2.games g

WHERE
  1 = 1
  AND g.id = {index}
  AND g.position = {position}
SELECT
  g.final_stack - g.stack AS stack_result

FROM
  {database}.games g

WHERE
  1 = 1
  AND g.id = {index}
  AND g.position = {position}
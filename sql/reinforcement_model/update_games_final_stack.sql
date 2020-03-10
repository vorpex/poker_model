UPDATE
  {database}.games g

SET
  g.final_stack = {final_stack}

WHERE
  1 = 1
  AND g.id = {index}
  AND g.uuid = '{uuid}'
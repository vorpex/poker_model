UPDATE
  {database}.games g

SET
  g.card1 = '{card1}',
  g.card2 = '{card2}',
  g.hand_db_format = '{hand_db_format}'

WHERE
  1 = 1
  AND g.id = {index}
  AND g.uuid = '{uuid}'
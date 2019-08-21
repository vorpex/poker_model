UPDATE
  poker_version2.games g

SET
  g.card1 = '{CARD1}',
  g.card2 = '{CARD2}',
  g.hand_db_format = '{HAND_DB_FORMAT}'

WHERE
  1 = 1
  AND g.id = {ID}
  AND g.player = '{PLAYER}'
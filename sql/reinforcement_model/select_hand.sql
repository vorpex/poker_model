SELECT
  g.hand_db_format,
  g.card1,
  g.card2

FROM
  {database}.games g

WHERE
  1 = 1
  AND g.id = {game_id}
  AND g.position = {position}
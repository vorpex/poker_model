SELECT
  g.hand_db_format

FROM
  poker_version2.games g

WHERE
  1 = 1
  AND g.id = {GAME_ID}
  AND g.position = {POSITION}
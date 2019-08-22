SELECT
  g.hand_db_format

FROM
  poker_version2.games g

WHERE
  1 = 1
  AND g.id = {game_id}
  AND g.position = {position}
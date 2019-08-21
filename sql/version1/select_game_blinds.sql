SELECT
  g.small_blind,
  g.big_blind

FROM
  poker_version1.games g

WHERE
  1 = 1
  AND g.id = {GAME_ID}
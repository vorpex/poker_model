SELECT
  h1.amount

FROM
  poker_version1.history h1

WHERE
  1 = 1
  AND h1.move IN ('small_blind', 'big_blind', 'raise')
  AND h1.game_id = {GAME_ID}
  AND h1.phase = {PHASE}
  AND h1.nr > (

  SELECT
    NVL(MAX(h2.nr), -1) AS max_player_nr

  FROM
    poker_version1.history h2

  WHERE
    1 = 1
    AND h2.game_id = {GAME_ID}
    AND h2.phase = {PHASE}
    AND h2.player_name = '{PLAYER_NAME}'

)

ORDER BY
  h1.nr DESC

LIMIT 1
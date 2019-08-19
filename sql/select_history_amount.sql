SELECT
  SUM(s.sum_amount) AS sum_amount

FROM (

  SELECT
    'raise' AS move_type,
    SUM(NVL(h1.amount, 0)) AS sum_amount

  FROM
    poker.history h1

  WHERE
    1 = 1
    AND h1.move = 'raise'
    AND h1.game_id = {GAME_ID}
    AND h1.phase = {PHASE}
    AND h1.nr > (

    SELECT
      NVL(MAX(h2.nr), -1) AS max_player_nr

    FROM
      poker.history h2

    WHERE
      1 = 1
      AND h2.game_id = {GAME_ID}
      AND h2.phase = {PHASE}
      AND h2.player_name = '{PLAYER_NAME}'

    )

  UNION

  SELECT
    'blind' AS move_type,
    MAX(NVL(h3.amount, 0)) AS sum_amount

  FROM
    poker.history h3

  WHERE
    1 = 1
    AND h3.move IN ('small_blind', 'big_blind')
    AND h3.game_id = {GAME_ID}
    AND h3.phase = {PHASE}
    AND h3.nr > (

    SELECT
      NVL(MAX(h4.nr), -1) AS max_player_nr

    FROM
      poker.history h4

    WHERE
      1 = 1
      AND h4.game_id = {GAME_ID}
      AND h4.phase = {PHASE}
      AND h4.player_name = '{PLAYER_NAME}'

    )

) s
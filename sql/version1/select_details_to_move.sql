SELECT
  a.move,
  b.flag

FROM (

  SELECT
    1 AS id,
    h.move AS move
  
  FROM
    poker.history h

  WHERE
    1 = 1
    AND h.game_id = {GAME_ID}
    AND h.phase = {PHASE}
    AND h.position = {POSITION}

  ORDER BY
    h.nr DESC
    
  LIMIT 1

) a

INNER JOIN (

  SELECT
    1 AS id,
    SUM(CASE WHEN h1.move IN ('small_blind', 'big_blind', 'raise') THEN 1 ELSE 0 END) AS flag

  FROM
    poker.history h1

  WHERE
    1 = 1
    AND h1.game_id = {GAME_ID}
    AND h1.phase = {PHASE}
    AND h1.nr > (

    SELECT
      MAX(h2.nr) AS max_nr
  
    FROM
      poker.history h2
  
    WHERE
      1 = 1
      AND h2.game_id = {GAME_ID}
      AND h2.phase = {PHASE}
      AND h2.position = {POSITION}
  
  )

) b
ON
  a.id = b.id
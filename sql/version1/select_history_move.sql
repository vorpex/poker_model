SELECT
  h.move

FROM
  poker_version1.history h

WHERE
  1 = 1
  AND h.game_id = {GAME_ID}
  AND h.phase = {PHASE}

ORDER BY
  h.nr DESC

LIMIT 1
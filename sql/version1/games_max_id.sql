SELECT
  NVL(MAX(g.id), -1) AS max_id

FROM
  poker_version1.games g
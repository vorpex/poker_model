SELECT
  CASE
    WHEN COUNT(1) - 2 * (SELECT COUNT(DISTINCT g.id) FROM games g) - (SELECT MAX(d.id) FROM decision_points d) >= 0 THEN 0
    ELSE 1
  END checksum_result

FROM
  history h
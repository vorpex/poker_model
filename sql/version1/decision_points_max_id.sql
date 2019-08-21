SELECT
  NVL(MAX(d.id), -1) AS max_id

FROM
  poker_version1.decision_points d
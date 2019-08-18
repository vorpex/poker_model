SELECT
  NVL(MAX(d.id), -1) AS max_id

FROM
  poker.decision_points d
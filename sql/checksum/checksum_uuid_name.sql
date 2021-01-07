SELECT
  SUM(substring(g.uuid, length(g.uuid), 1) - substring(g.name, length(g.name), 1)) AS checksum_result

FROM
  {database}.games g
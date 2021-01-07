SELECT
  SUM((SELECT t.player_num FROM {database}.games t WHERE 1 = 1 AND t.id = 1 AND t.uuid = 'uuid-0') - g.player_num) AS checksum_result

FROM
  {database}.games g
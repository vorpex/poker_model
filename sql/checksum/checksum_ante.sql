SELECT
  SUM((SELECT t.ante_amount FROM {database}.games t WHERE 1 = 1 AND t.id = 1 AND t.uuid = 'uuid-0') - g.ante_amount) AS checksum_result

FROM
  {database}.games g
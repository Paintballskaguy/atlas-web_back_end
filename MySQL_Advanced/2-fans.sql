-- Ranks the country origins of bands by total number of fans

SELECT origin, SUM(fans) AS NB_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;

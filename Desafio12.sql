/*
Desafío 12: SQL 2
*/
SELECT  re.[Name] country_name, cu.[Name] currency_name,  
		round( max(ra.AverageRate),2) currency_rate, round(avg(tr.TaxRate),2) average_tax_rate
  FROM [Person].[CountryRegion] re
  join [Person].[StateProvince] sp  on sp.CountryRegionCode = re.CountryRegionCode
  join [Sales].[CountryRegionCurrency] rc on rc.CountryRegionCode = re.CountryRegionCode
  join [Sales].[Currency] cu on cu.CurrencyCode = rc.CurrencyCode
  join [Sales].[SalesTaxRate] tr on tr.StateProvinceID = sp.StateProvinceID
  join [Sales].[CurrencyRate] ra on ra.[ToCurrencyCode] = rc.CurrencyCode
 GROUP BY re.[Name], cu.[Name]
 ORDER BY re.[Name], cu.[Name]
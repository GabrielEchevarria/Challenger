
-- Desafío 11: SQL 1
SELECT p.CountryRegionCode country_region_code, avg(tr.TaxRate) average_taxRate
  FROM [Sales].[SalesTaxRate] tr join [Person].[StateProvince] p
  on tr.StateProvinceID = p.StateProvinceID
  group by p.CountryRegionCode

GO


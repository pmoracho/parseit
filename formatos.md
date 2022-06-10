Formato   : sicore-retenciones-v2
Categoria : Afip.Sicore
Longitud  : 145

+-----+------------------------------+------------+--------+----------------------------+------------------+
|   # | Nombre del campo             |   Longitud | Tipo   | info adicional             | formato salida   |
|-----+------------------------------+------------+--------+----------------------------+------------------|
|   1 | Código comprobante           |          2 | table  | sicore-codigos-comprantes  |                  |
|   2 | Fecha de emisión             |         10 | date   | %d/%m/%Y                   | %d-%m-%Y         |
|   3 | Nro de Comprobante           |         16 | string |                            |                  |
|   4 | Importe del compr.           |         16 | amount |                            |                  |
|   5 | _                            |          1 | string |                            |                  |
|   6 | Código impuesto              |          3 | table  | sicore-codigos-impuestos   |                  |
|   7 | Código régimen               |          3 | string |                            |                  |
|   8 | Código operación             |          1 | table  | sicore-codigos-operaciones |                  |
|   9 | Base de cálculo              |         14 | amount |                            |                  |
|  10 | Fecha de emisión (retención) |         10 | date   | %d/%m/%Y                   | %d-%m-%Y         |
|  11 | Código condición             |          2 | table  | sicore-codigos-condiciones |                  |
|  12 | Ret.pract a suj.supendidos   |          1 | table  | sicore-reten-practicada    |                  |
|  13 | Importe de la retención      |         14 | amount |                            |                  |
|  14 | Porcentaje de exclusión      |          6 | amount |                            |                  |
|  15 | Fecha de emisión (boletín)   |         10 | date   | %d/%m/%Y                   | %d-%m-%Y         |
|  16 | Tipo doc. del retenido       |          2 | table  | sicore-tipos-documentos    |                  |
|  17 | Nro. doc. del retenido       |         20 | string |                            |                  |
|  18 | Nro. del certificado         |         14 | string |                            |                  |
+-----+------------------------------+------------+--------+----------------------------+------------------+

Formato   : sifere-retenciones
Categoria : Afip.Sifere
Longitud  : 79

+-----+--------------------------------+------------+--------+--------------------------+------------------+
|   # | Nombre del campo               |   Longitud | Tipo   | info adicional           | formato salida   |
|-----+--------------------------------+------------+--------+--------------------------+------------------|
|   1 | Código de Jurisdicción         |          3 | table  | sifere-jurisdicciones    |                  |
|   2 | CUIT del Agente de Retención   |         13 | string |                          |                  |
|   3 | Fecha de la Retención          |         10 | date   | %d/%m/%Y                 | %d-%m-%Y         |
|   4 | Número de Sucursal             |          4 | string |                          |                  |
|   5 | Número de constancia           |         16 | string |                          |                  |
|   6 | Tipo de Comprobante            |          1 | table  | sifere-tipo-comprobantes |                  |
|   7 | Letra del Comprobante          |          1 | string |                          |                  |
|   8 | Número de Comprobante Original |         20 | string |                          |                  |
|   9 | Importe Retenido               |         11 | amount |                          |                  |
+-----+--------------------------------+------------+--------+--------------------------+------------------+

Formato   : ventas-comprobantes
Categoria : Afip.Rg3685
Longitud  : 266

+-----+-------------------------------------------------------------------+------------+---------+--------------------------------+------------------+
|   # | Nombre del campo                                                  |   Longitud | Tipo    | info adicional                 | formato salida   |
|-----+-------------------------------------------------------------------+------------+---------+--------------------------------+------------------|
|   1 | Fecha del comprobante                                             |          8 | date    | %Y%m%d                         | %d-%m-%Y         |
|   2 | Tipo de comprobante                                               |          3 | table   | tipo_comprobante_comprasventas |                  |
|   3 | Punto de venta                                                    |          5 | string  |                                |                  |
|   4 | Número de Comprobante                                             |         20 | string  |                                |                  |
|   5 | Número de Comprobante hasta                                       |         20 | string  |                                |                  |
|   6 | Código de documento del comprador                                 |          2 | table   | tipo_documento_comprasventas   |                  |
|   7 | Número de identificación del comprador                            |         20 | string  |                                |                  |
|   8 | Apellido y nombres del comprador                                  |         30 | string  |                                |                  |
|   9 | Importe total de la operación                                     |         15 | zamount | 2                              |                  |
|  10 | Importe total de conceptos que no integran el precio neto gravado |         15 | zamount | 2                              |                  |
|  11 | Percepciones a no categorizados                                   |         15 | zamount | 2                              |                  |
|  12 | Importe de operaciones exentas                                    |         15 | zamount | 2                              |                  |
|  13 | Importe de percepciones o pagos a cuenta de impuestos nacionales  |         15 | zamount | 2                              |                  |
|  14 | Importe de percepciones de Ingresos Brutos                        |         15 | zamount | 2                              |                  |
|  15 | Importe de percepciones de Impuestos Municipales                  |         15 | zamount | 2                              |                  |
|  16 | Importe de Impuestos Internos                                     |         15 | zamount | 2                              |                  |
|  17 | Código de Moneda                                                  |          3 | table   | tipo_moneda_comprasventas      |                  |
|  18 | Tipo de Cambio                                                    |         10 | zamount | 6                              | 4.6f             |
|  19 | Cantidad de alícuotas de IVA                                      |          1 | string  |                                |                  |
|  20 | Código de operación                                               |          1 | string  |                                |                  |
|  21 | Otros Tributos                                                    |         15 | zamount | 2                              |                  |
|  22 | Dummy                                                             |          8 | string  | 2                              |                  |
+-----+-------------------------------------------------------------------+------------+---------+--------------------------------+------------------+

Formato   : compras-comprobantes
Categoria : Afip.Rg3685
Longitud  : 325

+-----+-------------------------------------------------------------------------+------------+---------+--------------------------------+------------------+
|   # | Nombre del campo                                                        |   Longitud | Tipo    | info adicional                 | formato salida   |
|-----+-------------------------------------------------------------------------+------------+---------+--------------------------------+------------------|
|   1 | Fecha del comprobante                                                   |          8 | date    | %Y%m%d                         | %d-%m-%Y         |
|   2 | Tipo de comprobante                                                     |          3 | table   | tipo_comprobante_comprasventas |                  |
|   3 | Punto de venta                                                          |          5 | string  |                                |                  |
|   4 | Número de Comprobante                                                   |         20 | string  |                                |                  |
|   5 | N° de despacho de Importación                                           |         16 | string  |                                |                  |
|   6 | Código de documento del Vendedor                                        |          2 | table   | tipo_documento_comprasventas   |                  |
|   7 | Número de identificación del vendedor                                   |         20 | string  |                                |                  |
|   8 | Apellido y nombres del vendedor                                         |         30 | string  |                                |                  |
|   9 | Importe total de la operación                                           |         15 | zamount | 2                              |                  |
|  10 | Importe total de conceptos que no integran el precio neto gravado       |         15 | zamount | 2                              |                  |
|  11 | Importe de operaciones exentas                                          |         15 | zamount | 2                              |                  |
|  12 | Importe de percepciones o pagos a cuenta del Impuesto al Valor Agregado |         15 | zamount | 2                              |                  |
|  13 | Importe de percepciones o pagos a cuenta de impuestos nacionales        |         15 | zamount | 2                              |                  |
|  14 | Importe de percepciones de Ingresos Brutos                              |         15 | zamount | 2                              |                  |
|  15 | Importe de percepciones de Impuestos Municipales                        |         15 | zamount | 2                              |                  |
|  16 | Importe de Impuestos Internos                                           |         15 | zamount | 2                              |                  |
|  17 | Código de Moneda                                                        |          3 | table   | tipo_moneda_comprasventas      |                  |
|  18 | Tipo de Cambio                                                          |         10 | zamount | 6                              | 4.6f             |
|  19 | Cantidad de alícuotas de IVA                                            |          1 | string  |                                |                  |
|  20 | Código de operación                                                     |          1 | string  |                                |                  |
|  21 | Crédito Fiscal Computable                                               |         15 | zamount | 2                              |                  |
|  22 | Otros Tributos                                                          |         15 | zamount | 2                              |                  |
|  23 | CUIT emisor/corredor                                                    |         11 | string  |                                |                  |
|  24 | Denominación del emisor/corredor                                        |         30 | string  |                                |                  |
|  25 | IVA comisión                                                            |         15 | zamount | 2                              |                  |
+-----+-------------------------------------------------------------------------+------------+---------+--------------------------------+------------------+

Formato   : Padron-iibb-general
Categoria : Agip.Padrones
Longitud  : 110

+-----+--------------------+------------+--------+-------------------+------------------+
|   # | Nombre del campo   |   Longitud | Tipo   | info adicional    | formato salida   |
|-----+--------------------+------------+--------+-------------------+------------------|
|   1 | Fecha Publ.        |          8 | date   | %d%m%Y            | %d-%m-%Y         |
|   2 | Fecha Desde        |          8 | date   | %d%m%Y            | %d-%m-%Y         |
|   3 | Fecha Hasta        |          8 | date   | %d%m%Y            | %d-%m-%Y         |
|   4 | CUIT               |         11 | string |                   |                  |
|   5 | Tipo               |          1 | table  | iibb-tipo-inscrip |                  |
|   6 | Marca Alta         |          1 | string |                   |                  |
|   7 | Marca Alícuota     |          1 | string |                   |                  |
|   8 | Percepción         |          4 | amount |                   |                  |
|   9 | Retención          |          4 | amount |                   |                  |
|  10 | Grupo Percep.      |          2 | string |                   |                  |
|  11 | Grupo Retención.   |          2 | string |                   |                  |
|  12 | Razón Social       |         60 | string |                   | %10s             |
+-----+--------------------+------------+--------+-------------------+------------------+

Formato   : compras-comprobantes-alicuotas
Categoria : Afip.Rg3685
Longitud  : 84

+-----+---------------------------------------+------------+---------+--------------------------------+------------------+
|   # | Nombre del campo                      |   Longitud | Tipo    | info adicional                 | formato salida   |
|-----+---------------------------------------+------------+---------+--------------------------------+------------------|
|   1 | Tipo de comprobante                   |          3 | table   | tipo_comprobante_comprasventas |                  |
|   2 | Punto de venta                        |          5 | string  |                                |                  |
|   3 | Número de Comprobante                 |         20 | string  |                                |                  |
|   4 | Código de documento del Vendedor      |          2 | table   | tipo_documento_comprasventas   |                  |
|   5 | Número de identificación del vendedor |         20 | string  |                                |                  |
|   6 | Importe neto gravado                  |         15 | zamount | 2                              |                  |
|   7 | Alicuota de Iva                       |          4 | table   | alicuotas_iva                  |                  |
|   8 | Impuesto liquidado                    |         15 | zamount | 2                              |                  |
+-----+---------------------------------------+------------+---------+--------------------------------+------------------+

Formato   : arciba-debitos
Categoria : Afip.Arciba
Longitud  : 215

+-----+--------------------------------------+------------+--------+------------------+------------------+
|   # | Nombre del campo                     |   Longitud | Tipo   | info adicional   | formato salida   |
|-----+--------------------------------------+------------+--------+------------------+------------------|
|   1 | Tipo de operación                    |          1 | table  | tipo_operacion   |                  |
|   2 | Código norma                         |          3 | string |                  |                  |
|   3 | Fecha de retención/percepción        |         10 | date   | %d/%m/%Y         | %d-%m-%Y         |
|   4 | Tipo comprobante Origen              |          2 | table  | tipo_comprobante |                  |
|   5 | Letra del Comprobante                |          1 | string |                  |                  |
|   6 | Nro de Comprobante                   |         16 | string |                  |                  |
|   7 | Fecha del comprobante                |         10 | date   | %d/%m/%Y         | %d-%m-%Y         |
|   8 | Monto del comprobante                |         16 | amount |                  |                  |
|   9 | Nro de certificado propio            |         16 | string |                  |                  |
|  10 | Tipo de documento del Retenido       |          1 | table  | tipo_documento   |                  |
|  11 | Nro de documento del Retenido        |         11 | string |                  |                  |
|  12 | Situación IB del Retenido            |          1 | table  | situacion_ib     |                  |
|  13 | Nro inscripción IB del Retenido      |         11 | string |                  |                  |
|  14 | Situación frente al Iva del Retenido |          1 | table  | situacion_iva    |                  |
|  15 | Razón social del Retenido            |         30 | string |                  |                  |
|  16 | Importe otros conceptos              |         16 | amount |                  |                  |
|  17 | Importe IVA                          |         16 | amount |                  |                  |
|  18 | Monto sujeto a Retención/Percepción  |         16 | amount |                  |                  |
|  19 | Alícuota                             |          5 | amount |                  |                  |
|  20 | Retención/Percepción practicada      |         16 | amount |                  |                  |
|  21 | Monto Total Retenido/Percibido       |         16 | amount |                  |                  |
+-----+--------------------------------------+------------+--------+------------------+------------------+

Formato   : ventas-comprobantes-alicuotas
Categoria : Afip.Rg3685
Longitud  : 62

+-----+-----------------------+------------+---------+--------------------------------+------------------+
|   # | Nombre del campo      |   Longitud | Tipo    | info adicional                 | formato salida   |
|-----+-----------------------+------------+---------+--------------------------------+------------------|
|   1 | Tipo de comprobante   |          3 | table   | tipo_comprobante_comprasventas |                  |
|   2 | Punto de venta        |          5 | string  |                                |                  |
|   3 | Número de Comprobante |         20 | string  |                                |                  |
|   4 | Importe neto gravado  |         15 | zamount | 2                              |                  |
|   5 | Alicuota de Iva       |          4 | table   | alicuotas_iva                  |                  |
|   6 | Impuesto liquidado    |         15 | zamount | 2                              |                  |
+-----+-----------------------+------------+---------+--------------------------------+------------------+

Formato   : sicore-retenciones
Categoria : Afip.Sicore
Longitud  : 144

+-----+------------------------------+------------+--------+----------------------------+------------------+
|   # | Nombre del campo             |   Longitud | Tipo   | info adicional             | formato salida   |
|-----+------------------------------+------------+--------+----------------------------+------------------|
|   1 | Código comprobante           |          2 | table  | sicore-codigos-comprantes  |                  |
|   2 | Fecha de emisión             |         10 | date   | %d/%m/%Y                   | %d-%m-%Y         |
|   3 | Nro de Comprobante           |         16 | string |                            |                  |
|   4 | Importe del compr.           |         16 | amount |                            |                  |
|   5 | Código impuesto              |          3 | table  | sicore-codigos-impuestos   |                  |
|   6 | Código régimen               |          3 | string |                            |                  |
|   7 | Código operación             |          1 | table  | sicore-codigos-operaciones |                  |
|   8 | Base de cálculo              |         14 | amount |                            |                  |
|   9 | Fecha de emisión (retención) |         10 | date   | %d/%m/%Y                   | %d-%m-%Y         |
|  10 | Código condición             |          2 | table  | sicore-codigos-condiciones |                  |
|  11 | Ret.pract a suj.supendidos   |          1 | table  | sicore-reten-practicada    |                  |
|  12 | Importe de la retención      |         14 | amount |                            |                  |
|  13 | Porcentaje de exclusión      |          6 | amount |                            |                  |
|  14 | Fecha de emisión (boletín)   |         10 | date   | %d/%m/%Y                   | %d-%m-%Y         |
|  15 | Tipo doc. del retenido       |          2 | table  | sicore-tipos-documentos    |                  |
|  16 | Nro. doc. del retenido       |         20 | string |                            |                  |
|  17 | Nro. del certificado         |         14 | string |                            |                  |
+-----+------------------------------+------------+--------+----------------------------+------------------+

Formato   : sifere-percepciones
Categoria : Afip.Sifere
Longitud  : 51

+-----+-------------------------------+------------+--------+--------------------------+------------------+
|   # | Nombre del campo              |   Longitud | Tipo   | info adicional           | formato salida   |
|-----+-------------------------------+------------+--------+--------------------------+------------------|
|   1 | Código de Jurisdicción        |          3 | table  | sifere-jurisdicciones    |                  |
|   2 | CUIT del Agente de Percepción |         13 | string |                          |                  |
|   3 | Fecha de la Percepción        |         10 | date   | %d/%m/%Y                 | %d-%m-%Y         |
|   4 | Número de Sucursal            |          4 | string |                          |                  |
|   5 | Número de constancia          |          8 | string |                          |                  |
|   6 | Tipo de Comprobante           |          1 | table  | sifere-tipo-comprobantes |                  |
|   7 | Letra del Comprobante         |          1 | string |                          |                  |
|   8 | Importe Percibido             |         11 | amount |                          |                  |
+-----+-------------------------------+------------+--------+--------------------------+------------------+

Formato   : sicore-sujetos
Categoria : Afip.Sicore
Longitud  : 83

+-----+--------------------+------------+--------+-------------------------+------------------+
|   # | Nombre del campo   |   Longitud | Tipo   | info adicional          | formato salida   |
|-----+--------------------+------------+--------+-------------------------+------------------|
|   1 | Nro. documento     |         11 | string |                         |                  |
|   2 | Razón Social       |         20 | string |                         |                  |
|   3 | Domicilio Fiscal   |         20 | string |                         |                  |
|   4 | Localidad          |         20 | string |                         |                  |
|   5 | Provincia          |          2 | table  | sicore-provincias       |                  |
|   6 | Código Postal      |          8 | string |                         |                  |
|   7 | Tipo documento     |          2 | table  | sicore-tipos-documentos |                  |
+-----+--------------------+------------+--------+-------------------------+------------------+

Formato   : arciba-creditos
Categoria : Afip.Arciba
Longitud  : 119

+-----+-------------------------------+------------+--------+------------------+------------------+
|   # | Nombre del campo              |   Longitud | Tipo   | info adicional   | formato salida   |
|-----+-------------------------------+------------+--------+------------------+------------------|
|   1 | Tipo de operación             |          1 | table  | tipo_operacion   |                  |
|   2 | Nro. Nota de crédito          |         12 | string |                  |                  |
|   3 | Fecha Nota de crédito         |         10 | date   | %d/%m/%Y         | %d-%m-%Y         |
|   4 | Monto Nota de crédito         |         16 | amount |                  |                  |
|   5 | Nro. certificado propio       |         16 | string |                  |                  |
|   6 | Tipo comprobante Origen       |          2 | table  | tipo_comprobante |                  |
|   7 | Letra del Comprobante         |          1 | string |                  |                  |
|   8 | Nro de Comprobante            |         16 | string |                  |                  |
|   9 | Nro de documento del Retenido |         11 | string |                  |                  |
|  10 | Código norma                  |          3 | string |                  |                  |
|  11 | Fecha de retención/percepción |         10 | date   | %d/%m/%Y         | %d-%m-%Y         |
|  12 | Ret/Perceo a deducir          |         16 | amount |                  |                  |
|  13 | Alícuota                      |          5 | amount |                  |                  |
+-----+-------------------------------+------------+--------+------------------+------------------+

Formato   : sire-2003
Categoria : Afip.Sire
Longitud  : 414

+-----+--------------------+------------+--------+------------------+------------------+
|   # | Nombre del campo   |   Longitud | Tipo   | info adicional   | formato salida   |
|-----+--------------------+------------+--------+------------------+------------------|
|   1 | Formulario         |          4 | string |                  |                  |
|   2 | Version            |          4 | string |                  |                  |
|   3 | CodTraz            |         10 | string |                  |                  |
|   4 | CuitAge            |         11 | string |                  |                  |
|   5 | Impuesto           |          3 | string |                  |                  |
|   6 | Regimen            |          3 | string |                  |                  |
|   7 | CuitOrd            |         11 | string |                  |                  |
|   8 | RetFecha           |         10 | string |                  |                  |
|   9 | CompTipo           |          2 | string |                  |                  |
|  10 | CompFecha          |         10 | string |                  |                  |
|  11 | ComoNro            |         16 | string |                  |                  |
|  12 | CompImporte        |         14 | string |                  |                  |
|  13 | Filler             |         14 | string |                  |                  |
|  14 | CertNro            |         25 | string |                  |                  |
|  15 | CertFecha          |         10 | string |                  |                  |
|  16 | CertImporte        |         14 | string |                  |                  |
|  17 | NcMotivo           |         30 | string |                  |                  |
|  18 | NoRet              |          1 | string |                  |                  |
|  19 | NoRetMotivo        |         30 | string |                  |                  |
|  20 | CDI                |          1 | string |                  |                  |
|  21 | CodAli             |          3 | string |                  |                  |
|  22 | Acrecen            |          1 | string |                  |                  |
|  23 | ClaveNIF           |         50 | string |                  |                  |
|  24 | Nombre             |         60 | string |                  |                  |
|  25 | Domic              |         60 | string |                  |                  |
|  26 | DomicPais          |          3 | string |                  |                  |
|  27 | TipPersona         |          1 | string |                  |                  |
|  28 | PaisNacConst       |          3 | string |                  |                  |
|  29 | FecNacConst        |         10 | date   | %d/%m/%Y         | %d-%m-%Y         |
+-----+--------------------+------------+--------+------------------+------------------+


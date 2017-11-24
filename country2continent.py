# Alpha-2 ISO country to continent
countriesAF = ['DZ', 'AO', 'SH', 'BJ', 'BW', 'BF', 'BI', 'CM', 'CV', 'CF', 'TD', 'KM', 'CG', 'CD', 'DJ', 'EG',
              'GQ', 'ER', 'ET', 'GA', 'GM', 'GH', 'GN', 'GW', 'CI', 'KE', 'LS', 'LR', 'LY', 'MG', 'MW', 'ML',
              'MR', 'MU', 'YT', 'MA', 'MZ', 'NA', 'NE', 'NG', 'ST', 'RE', 'RW', 'SN', 'SC', 'SL', 'SO', 'ZA',
              'SS', 'SD', 'SZ', 'TZ', 'TG', 'TN', 'UG', 'ZM', 'ZW']

countriesAT = ['AQ']

countriesAS = ['AF', 'AM', 'AZ', 'BH', 'BD', 'BT', 'BN', 'KH', 'CN', 'CX', 'CC', 'IO', 'GE', 'HK', 'IN', 'ID',
              'IR', 'IQ', 'IL', 'JP', 'JO', 'KZ', 'KW', 'KG', 'LA', 'LB', 'MO', 'MY', 'MV', 'MN', 'MM', 'NP',
              'KP', 'OM', 'PK', 'PS', 'PH', 'QA', 'SA', 'SG', 'KR', 'LK', 'SY', 'TW', 'TJ', 'TH', 'TR', 'TM',
              'AE', 'UZ', 'VN', 'YE']

countriesOC = ['AS', 'AU', 'NZ', 'CK', 'TL', 'FM', 'FJ', 'PF', 'GU', 'KI', 'MP', 'MH', 'UM', 'NR', 'NC', 'NU',
              'NF', 'PW', 'PG', 'WS', 'SB', 'TK', 'TO', 'TV', 'VU', 'WF']


countriesEU = ['AL', 'AD', 'AT', 'BY', 'BE', 'BA', 'BG', 'HR', 'CY', 'CZ', 'DK', 'EE', 'FO', 'FI', 'FR', 'DE',
              'GI', 'GR', 'HU', 'IS', 'IE', 'IM', 'IT', 'XK', 'LV', 'LI', 'LT', 'LU', 'MK', 'MT', 'MD', 'MC',
              'ME', 'NL', 'NO', 'PL', 'PT', 'RO', 'RU', 'SM', 'RS', 'SK', 'SI', 'ES', 'SE', 'CH', 'UA', 'GB',
              'VA']

countriesNA = ['AI', 'AG', 'AW', 'BS', 'BB', 'BZ', 'BM', 'BQ', 'VG', 'CA', 'KY', 'CR', 'CU', 'CW', 'DM', 'DO',
              'SV', 'GL', 'GD', 'GP', 'GT', 'HT', 'HN', 'JM', 'MQ', 'MX', 'PM', 'MS', 'KN', 'NI', 'PA', 'PR',
              'SX', 'LC', 'VC', 'TT', 'TC', 'US', 'VI']

countriesSA = ['AR', 'BO', 'BR', 'CL', 'CO', 'EC', 'FK', 'GF', 'GY', 'PY', 'PE', 'SR', 'UY', 'VE']

country2continent = dict().fromkeys(countriesAF, 'AF')
toAdd = dict().fromkeys(countriesAT, 'AT')
country2continent.update(toAdd)
toAdd = dict().fromkeys(countriesAS, 'AS')
country2continent.update(toAdd)
toAdd = dict().fromkeys(countriesOC, 'OC')
country2continent.update(toAdd)
toAdd = dict().fromkeys(countriesEU, 'EU')
country2continent.update(toAdd)
toAdd = dict().fromkeys(countriesNA, 'NA')
country2continent.update(toAdd)
toAdd = dict().fromkeys(countriesSA, 'SA')
country2continent.update(toAdd)
# print(country2continent)
# print(len(country2continent))
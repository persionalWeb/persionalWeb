from django.test import TestCase
import requests,re,json
from selenium import webdriver
# Create your tests here.

rawData=[['2019/09/25', 2093.935, 2087.316, 2082.949, 2113.052], ['2019/09/26', 2088.674, 2064.935, 2059.142, 2110.433], ['2019/09/27', 2064.521, 2062.853, 2029.345, 2078.324], ['2019/09/30', 2062.086, 2026.408, 2026.408, 2071.344], ['2019/10/08', 2027.339, 2031.007, 2027.339, 2062.897], ['2019/10/09', 2029.898, 2019.733, 1999.635, 2029.898], ['2019/10/10', 2009.728, 2031.238, 2000.083, 2031.876], ['2019/10/11', 2032.785, 2029.189, 2023.415, 2049.176], ['2019/10/14', 2040.952, 2039.215, 2032.177, 2046.642], ['2019/10/15', 2032.55, 2051.354, 2023.817, 2056.005], ['2019/10/16', 2039.93, 2028.342, 2025.738, 2039.93], ['2019/10/17', 2026.159, 2021.064, 2011.655, 2033.818], ['2019/10/18', 2006.607, 1990.059, 1983.442, 2018.473], ['2019/10/21', 1987.55, 1993.17, 1977.161, 1993.394], ['2019/10/22', 1992.217, 2000.356, 1984.478, 2001.685], ['2019/10/23', 1994.118, 1974.279, 1969.229, 2002.674], ['2019/10/24', 1973.983, 1955.768, 1951.608, 1974.766], ['2019/10/25', 1960.117, 1978.247, 1954.767, 1979.234], ['2019/10/28', 1976.395, 2011.691, 1976.059, 2013.765], ['2019/10/29', 2007.945, 2014.873, 2006.219, 2029.06], ['2019/10/30', 2007.381, 2003.73, 1987.378, 2007.381], ['2019/10/31', 2010.115, 1989.495, 1986.999, 2023.225], ['2019/11/01', 1988.844, 2011.313, 1979.162, 2016.13], ['2019/11/04', 2010.785, 2020.892, 2010.503, 2033.644], ['2019/11/05', 2024.127, 2021.531, 2011.969, 2030.316], ['2019/11/06', 2023.582, 2002.6, 1997.134, 2024.077], ['2019/11/07', 2005.983, 2018.867, 2002.479, 2018.867], ['2019/11/08', 2025.722, 2024.982, 2022.268, 2045.252], ['2019/11/11', 2017.991, 1982.767, 1976.914, 2017.991], ['2019/11/12', 1985.383, 1990.869, 1965.904, 1993.009], ['2019/11/13', 1991.207, 1999.546, 1989.088, 2008.897], ['2019/11/14', 2001.572, 2009.944, 1992.833, 2015.692], ['2019/11/15', 2008.378, 1993.538, 1993.538, 2014.461], ['2019/11/18', 1990.364, 1987.58, 1973.424, 1990.675], ['2019/11/19', 1990.668, 2009.089, 1987.318, 2009.089], ['2019/11/20', 2007.983, 1998.114, 1995.956, 2013.215], ['2019/11/21', 1994.547, 1992.712, 1986.576, 2001.888], ['2019/11/22', 1996.705, 1958.462, 1943.136, 2003.344], ['2019/11/25', 1954.148, 1954.296, 1925.81, 1955.086], ['2019/11/26', 1953.919, 1962.552, 1953.632, 1965.257], ['2019/11/27', 1962.422, 1960.969, 1952.393, 1971.612], ['2019/11/28', 1957.942, 1955.51, 1949.898, 1966.879], ['2019/11/29', 1950.282, 1929.601, 1913.865, 1950.282], ['2019/12/02', 1927.893, 1923.9, 1920.624, 1935.056], ['2019/12/03', 1919.601, 1930.393, 1904.596, 1930.393], ['2019/12/04', 1938.324, 1950.691, 1938.324, 1957.122], ['2019/12/05', 1949.511, 1958.36, 1946.16, 1959.72], ['2019/12/06', 1958.937, 1984.975, 1957.648, 1985.12], ['2019/12/09', 1984.934, 1975.102, 1971.244, 1987.616], ['2019/12/10', 1969.781, 1971.316, 1961.516, 1974.424], ['2019/12/11', 1970.683, 1962.804, 1957.079, 1971.483], ['2019/12/12', 1965.855, 1964.036, 1960.171, 1970.401], ['2019/12/13', 1970.867, 1988.276, 1970.475, 1989.234], ['2019/12/16', 1989.871, 1989.035, 1975.553, 1990.673], ['2019/12/17', 1990.634, 2003.945, 1987.76, 2005.494], ['2019/12/18', 2005.243, 2011.961, 2002.922, 2021.266], ['2019/12/19', 2013.714, 2010.177, 2001.788, 2013.714], ['2019/12/20', 2011.636, 2009.66, 2008.054, 2017.748], ['2019/12/23', 1990.532, 1980.632, 1978.486, 2007.019], ['2019/12/24', 1986.334, 2003.678, 1986.334, 2003.678], ['2019/12/25', 2008.919, 1982.336, 1975.012, 2008.919], ['2019/12/26', 1984.975, 2005.399, 1982.567, 2005.399], ['2019/12/27', 2009.053, 2002.356, 2001.201, 2025.529], ['2019/12/30', 1995.379, 2033.533, 1986.451, 2036.941], ['2019/12/31', 2032.728, 2037.242, 2024.479, 2038.138], ['2020/01/02', 2037.95, 2047.749, 2026.917, 2051.596], ['2020/01/03', 2046.183, 2038.135, 2029.539, 2046.697], ['2020/01/06', 2028.844, 2028.684, 2015.19, 2036.327], ['2020/01/07', 2029.672, 2052.982, 2028.785, 2052.982], ['2020/01/08', 2043.536, 2027.953, 2023.739, 2048.939], ['2020/01/09', 2036.165, 2062.048, 2036.165, 2065.528], ['2020/01/10', 2064.686, 2100.447, 2064.686, 2104.2], ['2020/01/13', 2099.736, 2116.162, 2098.138, 2122.416], ['2020/01/14', 2115.89, 2094.735, 2090.485, 2115.916], ['2020/01/15', 2093.09, 2097.72, 2088.019, 2113.063], ['2020/01/16', 2099.771, 2098.207, 2092.323, 2105.72], ['2020/01/17', 2104.582, 2094.628, 2091.125, 2108.831], ['2020/01/20', 2095.288, 2089.265, 2078.181, 2096.704], ['2020/01/21', 2078.412, 2038.129, 2038.024, 2078.412], ['2020/01/22', 2029.126, 2036.465, 2002.844, 2042.494], ['2020/01/23', 2023.602, 1961.663, 1949.123, 2025.448], ['2020/02/03', 1780.144, 1778.502, 1776.945, 1780.354], ['2020/02/04', 1680.73, 1740.958, 1680.73, 1747.457], ['2020/02/05', 1740.294, 1759.147, 1732.926, 1777.744], ['2020/02/06', 1759.319, 1781.276, 1745.061, 1783.973], ['2020/02/07', 1777.03, 1794.868, 1765.971, 1794.868], ['2020/02/10', 1785.343, 1824.276, 1774.763, 1825.148], ['2020/02/11', 1824.209, 1849.08, 1823.467, 1864.123], ['2020/02/12', 1847.386, 1857.949, 1839.33, 1858.482], ['2020/02/13', 1856.325, 1835.06, 1831.342, 1868.158], ['2020/02/14', 1829.157, 1828.511, 1817.411, 1837.962], ['2020/02/17', 1829.859, 1862.984, 1829.804, 1863.76], ['2020/02/18', 1865.277, 1868.869, 1851.771, 1869.243], ['2020/02/19', 1866.031, 1879.023, 1859.37, 1889.115], ['2020/02/20', 1878.494, 1927.903, 1878.347, 1928.83], ['2020/02/21', 1921.627, 1925.481, 1917.024, 1930.666], ['2020/02/24', 1914.75, 1906.877, 1887.885, 1914.75], ['2020/02/25', 1873.97, 1881.193, 1842.433, 1886.69], ['2020/02/26', 1862.179, 1867.212, 1854.523, 1890.602], ['2020/02/27', 1870.036, 1882.459, 1870.036, 1894.435], ['2020/02/28', 1838.424, 1796.079, 1794.679, 1845.771], ['2020/03/02', 1794.995, 1841.056, 1794.995, 1845.96], ['2020/03/03', 1855.679, 1857.802, 1847.082, 1870.297], ['2020/03/04', 1850.776, 1877.746, 1849.356, 1877.746], ['2020/03/05', 1886.403, 1949.585, 1886.403, 1956.261], ['2020/03/06', 1928.542, 1929.499, 1923.921, 1952.475], ['2020/03/09', 1902.953, 1864.448, 1861.404, 1902.953], ['2020/03/10', 1839.498, 1897.784, 1831.864, 1897.784], ['2020/03/11', 1899.219, 1898.327, 1893.748, 1927.625], ['2020/03/12', 1877.729, 1862.023, 1852.584, 1877.729], ['2020/03/13', 1780.716, 1843.433, 1775.385, 1850.45], ['2020/03/16', 1849.277, 1793.698, 1789.248, 1856.826], ['2020/03/17', 1788.26, 1763.464, 1719.464, 1808.437], ['2020/03/18', 1773.299, 1719.386, 1719.212, 1788.746], ['2020/03/19', 1712.354, 1694.655, 1655.554, 1719.787], ['2020/03/20', 1709.114, 1734.046, 1702.934, 1736.455], ['2020/03/23', 1694.271, 1681.891, 1676.838, 1709.579], ['2020/03/24', 1712.633, 1739.748, 1701.304, 1740.552], ['2020/03/25', 1775.006, 1781.609, 1758.671, 1785.489], ['2020/03/26', 1772.248, 1787.873, 1763.453, 1802.982], ['2020/03/27', 1804.715, 1806.636, 1804.584, 1829.118], ['2020/03/30', 1787.67, 1789.717, 1779.73, 1796.945], ['2020/03/31', 1803.069, 1822.016, 1796.956, 1826.239], ['2020/04/01', 1817.678, 1800.471, 1797.315, 1826.349], ['2020/04/02', 1787.85, 1815.197, 1784.815, 1815.197], ['2020/04/03', 1811.81, 1820.479, 1809.888, 1837.131], ['2020/04/07', 1844.355, 1869.159, 1844.355, 1875.532], ['2020/04/08', 1864.883, 1871.624, 1862.404, 1877.378], ['2020/04/09', 1877.373, 1881.238, 1868.046, 1887.934], ['2020/04/10', 1879.759, 1867.163, 1863.87, 1905.667], ['2020/04/13', 1856.509, 1852.775, 1839.208, 1863.197], ['2020/04/14', 1859.708, 1873.177, 1851.002, 1873.827], ['2020/04/15', 1874.109, 1855.268, 1853.976, 1878.841], ['2020/04/16', 1847.194, 1843.072, 1836.546, 1850.491], ['2020/04/17', 1853.358, 1852.816, 1848.745, 1871.216], ['2020/04/20', 1856.747, 1875.225, 1849.986, 1875.225], ['2020/04/21', 1868.151, 1851.343, 1839.259, 1868.266], ['2020/04/22', 1844.698, 1898.314, 1837.382, 1898.314], ['2020/04/23', 1898.761, 1902.74, 1898.287, 1921.085], ['2020/04/24', 1914.121, 1919.276, 1901.477, 1933.896]]
categoryData = []
values = []
for i in range(len(rawData)):
    categoryData.append(rawData[i].splice(0, 1)[0]);
    values.append(rawData[i])
print(categoryData)
print(values)

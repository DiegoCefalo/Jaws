![tiburon](https://github.com/SweetBabyJezuz/Jaws/blob/master/src/jaws.jpg)
# Jaws
En este repositorio se encuentra un breve análisis estadístico sobre reportes de ataques de tiburones. Los datos fueron obtenidos de:
* [Datos tiburon](https://www.kaggle.com/teajay/global-shark-attacks)

    Puesto a que el dataset obtenido carece de datos útiles bien estructurados, se tuvo que realizar una limpieza extensa de estos. Primero se desecharon las filas completamente vacías. Luego se desecharon las columnas irrelevantes al análisis. La información del dataset manipulada fue esencialmente la edad y el sexo de la víctima, el país, el año y la época del año de los casos reportados. El resto de datos han sido si acaso mínimamente modificados. Debido a que los pasos detallados de todo el proceso son muy extensos, si posees interés en ello, el procedimiento se encuentran documentado en el archivo clean.ipynb de este repositorio.
## Hipótesis
 Si eres un hombre joven en Estados Unidos, tienes la mayor probabilidad de ser atacado por un tiburón.
## Datos Resaltantes
 Como muestra la siguiente gráfica, según los datos obtenidos, la mayoría de los ataques de tiburón han sido a jóvenes de 16 a 20 años. El pico a los 27 años se produjo por falta de datos, que fueron rellenados con la media estadística, aunque claramente de puede apreciar el patrón descrito.
![edad](https://github.com/SweetBabyJezuz/Jaws/blob/master/img/edad.jpg)
 Luego, se puede observar que la mayoría de los ataques fueron a hombres (casi 8 veces más). Afortunadamente para ambos, la probabilidad de sobrevivir a uno de estos ataques es mucho mas alta que la de morir.
![genero](https://github.com/SweetBabyJezuz/Jaws/blob/master/img/genero.jpg)
 También se puede apreciar que la mayoría de los ataques se produjeron en Estados Unidos.
![paises](https://github.com/SweetBabyJezuz/Jaws/blob/master/img/paises.jpg)
 Un patrón interesante es que el número de reportes ha aumentado con los años. Sin embargo esto no significa que ahora los tiburones atacan mas seguido, sino que ha mejorado la documentación de estos casos.
![año](https://github.com/SweetBabyJezuz/Jaws/blob/master/img/a%C3%B1o.jpg)
 Finalmente, como era de esperarse, en verano (tanto cuando es en el hemisferio norte como en el sur) aumenta el número de reportes porque hay mas gente en la playa.
![epoca](https://github.com/SweetBabyJezuz/Jaws/blob/master/img/epoca.jpg)
 En el gráfico de arriba S significa hemisferio sur y N significa hemisferio norte.
 
## Conclusión
 Si cumples con aunque sea alguna de las condiciones anteriores, es recomendable llevarse un repelente de tiburones a la playa. Para mas información, remitirse al archivo analysis.ipynb de este repositorio.
 ## Documentación de módulos utilizados
 * [Pandas](https://pandas.pydata.org/docs/)
 * [Numpy](https://numpy.org/doc/stable/)
 * [Plotly](https://plotly.com/python/)
 * [Seaborn](https://seaborn.pydata.org/)
 * [Matplotlib](https://matplotlib.org/stable/index.html)
 * [Regular Expressions](https://docs.python.org/3/library/re.html)
 * [Geopy](https://geopy.readthedocs.io/en/stable/)
import pandas as pd

#questão 1
seriesAno1 = {'Java': 16.25, 'C': 16.04, 'Python': 9.85}
seriesAno2 = {'C': 16.21, 'Python': 12.12, 'Java': 11.68}

series1 = pd.Series(seriesAno1)
series2 = pd.Series(seriesAno2)

#questão 2
print(f"a soma das linguagens no ano 1 é {series1.sum()}%")
print(f"a soma das linguagens no ano 2 é {series2.sum()}%")

#questão 3
print(series2.sub(series1, fill_value=0))

#questão 4
print(series2.sub(series1, fill_value=0)[series2.sub(series1, fill_value=0) > 0])

#questão 5
series_estimated = series2 + series2.sub(series1, fill_value=0) * 2

print(series_estimated.nlargest(1))
# Plot the raw values over time
prices.plot()
plt.show()


# Scatterplot with one company per axis
print(prices.columns)
prices.plot.scatter('EBAY', 'YHOO')
plt.show()

# Scatterplot with color relating to time
prices.plot.scatter('EBAY', 'YHOO', c=prices.index, 
                    cmap=plt.cm.viridis, colorbar=False)
plt.show()
